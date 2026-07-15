from pathlib import Path

from ai.embeddings.embedding_service import (
    EmbeddingService
)

from ai.rag.policy_faiss_service import (
    PolicyFaissService
)

from ai.vector_store.policy_vector_store import (
    policy_vector_store
)

from common.logger import logger


class PolicyLoader:

    @staticmethod
    def load():

        # Already indexed
        if (
            PolicyFaissService.exists()
            and
            PolicyFaissService.total_vectors() > 0
            and
            policy_vector_store.documents
        ):

            logger.info(
                "Policy index already exists. Skipping embedding generation."
            )

            return

        logger.info(
            "Creating policy vector index..."
        )

        file_path = (
            Path(__file__).parent
            / "policy.txt"
        )

        text = file_path.read_text(
            encoding="utf-8"
        )

        policies = [

            policy.strip()

            for policy in text.split(
                "------------------------------------------------"
            )

            if policy.strip()

        ]

        embeddings = []

        for policy in policies:

            embedding = (
                EmbeddingService.generate(
                    policy
                )
            )

            embeddings.append(
                embedding
            )

        policy_vector_store.create(

            embeddings,

            policies

        )

        logger.info(
            "Policy vector index created successfully."
        )