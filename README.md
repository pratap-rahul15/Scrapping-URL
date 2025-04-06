
# Scrapping-URL

A full-stack web application that allows users to input a website URL and a query then returns the top 10 most relevant HTML content chunks using semantic search powered by embeddings and a vector database.
---

## 🚀 Overview

This application performs real-time:
- Web scraping from the provided URL
- Text chunking and embedding using sentence-transformers
- Semantic search via a vector database (Weaviate)
- Ranks and displays the most relevant HTML sections for the user’s query

---


## ✅ Prerequisites

Install the following before setup:

- **[Node.js](https://nodejs.org/)** (v16+)
- **[Python 3.9+](https://www.python.org/)**
- **[Docker](https://www.docker.com/)** (for vector DB)
- **pip** and **virtualenv** (Python tools)

---

## ⚙️ Setup & Run Locally

### 🔹 Frontend (React + Vite)

```bash
cd client
npm install
npm run dev

Visit the app at: http://localhost:5173
```


### 🐳 Start Vector Database (Weaviate)

Before running the backend, you need to start the vector database.

This project uses **Weaviate**, set up via Docker Compose.

Spin it up using the following command:

```
docker-compose -f weaviate-client.yml up --build -d


### 🔸 Backend (FastAPI)

cd server
python -m venv venv
source venv/bin/activate     
pip install -r requirements.txt

```

### Run the FastAPI server:

```
uvicorn main:app --reload --port 8000
```

### 📍 API will be live at:
```
http://localhost:8000

```

###  🔬 You can also explore and test the endpoints using FastAPI's built-in Swagger UI:
```
http://localhost:8000/docs

```

###  🛠 Technologies Used

```
Frontend

React.js

Vite

Tailwind CSS

Axios

-----------------

Backend

FastAPI

BeautifulSoup

SentenceTransformers

Weaviate (vector DB)

Uvicorn (ASGI server)

```

### 📸 Usage Flow

-  Open: http://localhost:5173

-  Enter a public website URL

-  Enter your search query

-  See top 10 relevant content chunks instantly!

  ### 🧠 Core Logic
🔍 Step-by-Step Flow 
- Scraping:

  Uses requests and BeautifulSoup to parse the page content 

- Chunking:

  HTML text is split into logical text chunks using custom   token-based logic.

- Embedding:

Each chunk is converted to a vector using sentence-transformers.

- Vector DB Insertion:

Chunks are stored in Weaviate as embeddings.

-  Semantic Search:

Query is embedded and matched against stored vectors to find   top 10 results.

- Response:

The 10 most relevant chunks are sent back and rendered in the frontend.

![Screenshot (223)](https://github.com/user-attachments/assets/68995a96-9dbf-4744-83ed-5e8f2b223cd1)

