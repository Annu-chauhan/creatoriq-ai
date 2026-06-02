from app.services.embedding_service import (
    create_embeddings
)

from app.services.qdrant_service import (
    search_chunks
)


def retrieve_context(question):

    print("QUESTION:", question)

    query_embedding = create_embeddings(
        [question]
    )[0]

    results = search_chunks(
        query_embedding,
        limit=5
    )

    print("RESULTS:", results)

    context = ""

    sources = []

    for result in results:

        context += (
            result["chunk"]
            + "\n\n"
        )

        sources.append(
            f'Video {result["video_id"]} - Chunk {result["chunk_id"]}'
        )

    print("CONTEXT:", context)
    print("SOURCES:", sources)

    return {
        "context": context,
        "sources": sources
    }