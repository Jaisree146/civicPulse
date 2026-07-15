import json
import os

from ai.rag.policy_faiss_service import (
    PolicyFaissService
)


class PolicyVectorStore:

    STORAGE_DIR = "storage"

    DOCUMENT_FILE = os.path.join(
        STORAGE_DIR,
        "policies.json"
    )

    def __init__(self):

        self.documents = []

        self.load_documents()

    def create(
        self,
        embeddings: list,
        documents: list[str]
    ):

        self.documents = documents

        self.save_documents()

        for embedding in embeddings:

            PolicyFaissService.add(
                embedding
            )

        PolicyFaissService.save()

    def search(
        self,
        embedding: list[float],
        k: int = 5
    ):

        scores, indices = (
            PolicyFaissService.search(
                embedding,
                k
            )
        )

        results = []

        for score, index in zip(
            scores,
            indices
        ):

            if index == -1:
                continue

            results.append(
                {
                    "text": self.documents[index],
                    "score": score
                }
            )

        return results

    def save_documents(self):

        os.makedirs(
            self.STORAGE_DIR,
            exist_ok=True
        )

        with open(
            self.DOCUMENT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.documents,
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_documents(self):

        if not os.path.exists(
            self.DOCUMENT_FILE
        ):

            return

        with open(
            self.DOCUMENT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            self.documents = json.load(
                file
            )


policy_vector_store = PolicyVectorStore()