
import uuid
from weaviate.classes.config import Configure, Property, DataType

def init_chunk_collection(client):
    if client.collections.exists("Chunk"):
        client.collections.delete("Chunk")

    client.collections.create(
        name="Chunk",
        properties=[
            Property(name="text", data_type=DataType.TEXT)
        ],
        vector_index_config=Configure.VectorIndex.hnsw(),  # No args here
        vectorizer_config=Configure.Vectorizer.none()
    )

    return client.collections.get("Chunk")


def upsert_chunks(collection, chunks, embeddings):
    for chunk, embedding in zip(chunks, embeddings):
        collection.data.insert(
            properties={"text": chunk},
            vector=embedding,
            uuid=uuid.uuid4()
        )

def query_chunks(collection, query_embedding):
    results = collection.query.near_vector(query_embedding, limit=10)
    return [{"chunk": obj.properties["text"]} for obj in results.objects]
