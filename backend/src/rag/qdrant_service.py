from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from src.rag.embeddings import generate_embedding


COLLECTION_NAME = "rag_documents"


class QdrantRAG:
    def __init__(self):
        self.client = QdrantClient(host="localhost", port=6333)

        # Crear colección si no existe
        if COLLECTION_NAME not in [col.name for col in self.client.get_collections().collections]:
            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE)
            )

    def add_document(self, content: str):
        vector = generate_embedding(content)

        point = PointStruct(
            id=None,
            vector=vector,
            payload={"text": content}
        )

        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=[point]
        )

    def search(self, query: str, limit: int = 3):
        vector = generate_embedding(query)

        results = self.client.search(
            collection_name=COLLECTION_NAME,
            query_vector=vector,
            limit=limit
        )

        return [hit.payload["text"] for hit in results]
