# CreatorIQ AI

CreatorIQ AI is an AI, vector search, and RAG (Retrieval-Augmented Generation) analytics Creator Intelligence Platform for YouTube videos and Instagram Reels.

We developed this project as part of a technical challenge to prove that creator content can be converted to searchable knowledge, and acted upon to inform action.

The purpose wasn't only to create a chatbot, it was to make something a creator would be able to use to learn how people of the world listen to them, compare their content in different ways and get ideas for their future videos.

---

## What It Does

If you are provided with a video from YouTube or Instagram Reel, the platform:

Extracts a transcript and metadata.
* Calculates engagement metrics
Chunks from the text are stored in a vector database.The chunks from the text are stored in a vector database.
Lets users call AI Chat on the material
* Compares videos side-by-side
* Proposes content ideas and creator insights to guide crafting content

---

## Features

### Creator Dashboard

Create a summary of a creator's content, quickly:

* Health Score
* Growth Score
* Brand Match Score
* Creator Analysis
* Audience Analysis
* Content Summary

### Video Metadata

Automatically extracts:

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

Make inquiries like:

What primarily is this creator being referred to?
Which brand(s) would fit this guy?
Which topics seem to be the most frequently covered in the publications?

Responses are created based on retrieved chunks and reference(s) to the source.

### Video Comparison

Analyse and interpret similarities and differences between two video clips;

Why the other did better
* Differences in hooks
* Audience appeal
* Content structure
* Engagement drivers

### Content Strategy

Generate:

* Better hooks
* Future content ideas
* Viral moments
* Stronger titles
* Content improvements

---

## Tech Stack

Frontend:

* Next.js
* React
* TypeScript

Backend:

* FastAPI
* Python

AI Layer:

* LangGraph
* Gemini

Vector Database:

* Qdrant

Embeddings:

* Sentence Transformers

Transcript Extraction:

* youtube-transcript-api
* yt-dlp
* Instaloader

---

## How It Works

The process is very simple:

User enters URL of a video.User types in URL of a video.
The second step is to extract transcript and metadata.The second step involves the removal of transcript and metadata.
3. Break apart transcript into segments
4. Chunks is transformed into embeddings
6. All embeddings are stored in Qdrant.
6. Customer inquires of a question
Information files are retrieved 7. Relevant chunks
- 8. Gemini generates an answer with retrieved context

This ensures the use of real video content rather than only the language model in answering questions.

---

So why did I choose this architecture?Why choose this architecture?

Since I wanted to use a lightweight, fast, locally accessible, and metadata filterable database, I chose Qdrant.

LangGraph simplified multi-step workflows and the ability to retain the history of a chat.

The decision to use FastAPI was made because it's easy to use, fast and compatible with AI applications.

In order to achieve this it was decided not to over engineer the system to achieve simplicity, reliability and low cost.

---

## Scaling Thoughts

If this was to run thousands of creators every day:

Embeddings would be called/created only once at ingestion time.
Vectors would be permanently stored in Qdrant.Qdrant would be storing vectors forever.
The metadata may be able to be cached.
Transfer of the food may occur independently of the others
In addition to that, an instance of FastAPI might be able to scale horizontally.

This helps to ensure smooth retrieval speeds and ensures costs stay manageable.

---

## Running Locally

Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Environment Variables

```env
GEMINI_API_KEY=your_key_here
QDRANT_URL=http://localhost:6333
```

---

## Future Improvements

If I continued on this project the things that I would add are:

* User authentication
* Creator history tracking
* Better Instagram analytics
* Real-time streaming responses
* Multi-video knowledge base
* Team collaboration features

---

## Demo

The demo covers:

* Creator Dashboard
* AI Chat
* Video Comparison
* Content Strategy
* Instagram Reel Analysis
* Source-based RAG Responses

---

Designed by Parul Chauhan