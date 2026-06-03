# CreatorIQ AI

CreatorIQ AI is a creator intelligence platform which enables the analysis of YouTube videos and Instagram Reels with the help of AI, vector search, and Retrieval-Augmented Generation (RAG).

This project aims to improve content creators' awareness of video performance, enable video comparisons, provide key learnings and engage with their content through AI-driven chat.

---

## Features

### Creator Dashboard

* Health Score
* Growth Score
* Brand Score
* Creator Analysis
* Audience Analysis
* Dashboard Summary

### Metadata Extraction

* Creator Name
* Followers
* Views
* Likes
* Comments
* Upload Date
* Duration
* Hashtags
* Engagement Rate

### AI Chat

* LangGraph-powered workflow
* Context-aware responses
* Source citations
* Conversation memory

### Video Comparison

* Compare two videos
* Engagement analysis
* Performance comparison
* AI-generated recommendations

### AI Content Strategist

* Better hooks
* Content ideas
* Growth opportunities
* Improvement suggestions

### Platform Support

* YouTube Videos
* Instagram Reels

---

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript

### Backend

* FastAPI
* Python

### AI Layer

* LangGraph
* Gemini

### Vector Database

* Qdrant

### Embeddings

* Sentence Transformers

---

## System Architecture

![System Architecture](![Acrhitecture](image.png))

### Flow

1. The user enters a URL of a YouTube or Instagram video.
2. Metadata and transcripts are stripped off.
3. Analytics are calculated which include engagement rate.
4. Chunk of text is converted to embedding.
5. Embeddings are saved in Qdrant.
6. The relevant chunks are retrieved using the semantic search.
7. LangGraph is responsible for retrieval, memory and response generation.
8. Gemini produces sensible reactions.
9. Results are shown in the frontend.
---

## Why This Architecture?

What I wanted to do, is create a system that could scale and be cost friendly at the same time.

Embeddings are created once upon ingestion and will always stay in Qdrant.

New queries use the same vectors as those in earlier queries, reducing inference costs and/or maintaining high query speed.

---

## Running Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Environment Variables

```env
GEMINI_API_KEY=your_gemini_api_key

QDRANT_URL=- 
 -Local:         http://localhost:3000
- Network:       http://192.168.29.2:3000

QDRANT_COLLECTION=video_chunks
```

---

## Scalability

To help thousands of people develop their abilities:

* Generate embeddings once
To avoid duplification of vector operations, reuse vectors for future operations where possible.
* Cache metadata
* Scale FastAPI horizontally
Ingest data into pipelines asynchronously.Asynchronously ingest data into pipelines.

This approach reduce the cost but with high quality retrieval and generation of response.

---

## Author

Parul Chauhan

CreatorIQ AI – Engineering Challenge Submission