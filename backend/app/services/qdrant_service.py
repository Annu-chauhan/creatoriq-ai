from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
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
def store_chunks(chunks, embeddings, video_id):

    points = []

    for chunk, embedding in zip(chunks, embeddings):

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "video_id": video_id,
                    "text": chunk
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    return len(points)