from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from weaviate import connect_to_local

from app.scraper import fetch_and_clean_html
from app.chunker import chunk_text
from app.embedder import embed_texts
from app.vector_db import init_chunk_collection, upsert_chunks, query_chunks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    url: str
    query: str

@app.post("/search")
async def search(request: SearchRequest):
    client = connect_to_local()  # Step 1: Connect to Weaviate
    try:
        # Step 2: Create/init the collection
        collection = init_chunk_collection(client)

        text = fetch_and_clean_html(request.url)
        
        chunks = chunk_text(text)
        chunk_texts = [chunk["text"] for chunk in chunks]
        
        chunk_embeddings = embed_texts(chunk_texts)

        # upsert with chunk["text"] for embedding, but return both
        upsert_chunks(collection, chunk_texts, chunk_embeddings)

        query_embedding = embed_texts([request.query])[0]
        results = query_chunks(collection, query_embedding)

        # Attach raw HTML to results
        final_results = []
        for i, result in enumerate(results):
            final_results.append({
                "text": chunks[i]["text"],
                "html": chunks[i]["html"]
            })

        return final_results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        client.close()  #Step 9: Close the connection
