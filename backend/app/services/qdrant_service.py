from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

import uuid

client = QdrantClient(":memory:")

COLLECTION_NAME = "video_chunks"


def create_collection():

    collections = client.get_collections().collections

    collection_names = [
        collection.name
        for collection in collections
    ]

    if COLLECTION_NAME not in collection_names:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    return True


def store_chunks(
    chunks,
    embeddings,
    video_id,
    metadata=None
):

    create_collection()

    if metadata is None:
        metadata = {}

    points = []

    for idx, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "video_id": video_id,
                    "chunk_id": idx,
                    "chunk": chunk,

                    # metadata
                    "creator": metadata.get("creator"),
                    "views": metadata.get("views"),
                    "likes": metadata.get("likes"),
                    "comments": metadata.get("comments"),
                    "duration": metadata.get("duration"),
                    "upload_date": metadata.get("upload_date"),
                    "hashtags": metadata.get("hashtags"),
                    "engagement_rate": metadata.get(
                        "engagement_rate"
                    )
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    return len(points)


def search_chunks(
    query_embedding,
    limit=5
):

    create_collection()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=limit
    )

    return [
        {
            "video_id": point.payload.get("video_id"),
            "chunk_id": point.payload.get("chunk_id"),
            "chunk": point.payload.get("chunk"),

            "creator": point.payload.get("creator"),
            "views": point.payload.get("views"),
            "likes": point.payload.get("likes"),
            "comments": point.payload.get("comments"),
            "duration": point.payload.get("duration"),
            "upload_date": point.payload.get("upload_date"),
            "hashtags": point.payload.get("hashtags"),
            "engagement_rate": point.payload.get(
                "engagement_rate"
            )
        }
        for point in results.points
    ]