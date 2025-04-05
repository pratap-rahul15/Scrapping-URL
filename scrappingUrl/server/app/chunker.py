from transformers import AutoTokenizer
from bs4 import BeautifulSoup
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def chunk_text(raw_html: str, max_tokens=500):
    encoding = tokenizer(
        raw_html,
        return_offsets_mapping=True,
        add_special_tokens=False
    )

    input_ids = encoding["input_ids"]
    offsets = encoding["offset_mapping"]
    chunks = []

    for i in range(0, len(input_ids), max_tokens):
        chunk_ids = input_ids[i:i + max_tokens]
        chunk_offsets = offsets[i:i + max_tokens]

        # Get the character span of the current chunk
        start_char = chunk_offsets[0][0]
        end_char = chunk_offsets[-1][1]

        html_chunk = raw_html[start_char:end_char]

        # Clean text from HTML using BeautifulSoup
        # soup = BeautifulSoup(html_chunk, "html.parser")
        # text_chunk = soup.get_text(separator=" ", strip=True)
        soup = BeautifulSoup(html_chunk, "html.parser")

        # Try to extract body content if possible
        if soup.body:
            text_chunk = soup.body.get_text(separator=" ", strip=True)
        else:
            text_chunk = soup.get_text(separator=" ", strip=True)

        chunks.append({
            "text": text_chunk,
            "html": html_chunk
        })


    return chunks
