import re

from ai.embeddings.embedding_service import (
    EmbeddingService
)

from ai.vector_store.policy_vector_store import (
    policy_vector_store
)


class RagService:

    @staticmethod
    def retrieve(
        query: str,
        k: int = 3
    ):

        embedding = EmbeddingService.generate(
            query
        )

        return policy_vector_store.search(
            embedding,
            k
        )

    @staticmethod
    def retrieve_policy(
        category: str
    ):

        results = RagService.retrieve(

            f"{category} resolution policy",

            k=1

        )

        if not results:

            return {

                "category": category,

                "resolution_days": None,

                "policy": "No municipal policy found."

            }

        policy = results[0]["text"]

        match = re.search(

            r"within\s+(\d+)\s+working\s+days",

            policy,

            re.IGNORECASE

        )

        resolution_days = (

            int(match.group(1))

            if match

            else None

        )

        return {

            "category": category,

            "resolution_days": resolution_days,

            "policy": policy

        }