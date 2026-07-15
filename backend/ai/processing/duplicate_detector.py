import faiss
import numpy as np

from ai.embeddings.embedding_service import EmbeddingService
from repositories.issue_repository import IssueRepository


class DuplicateDetector:

    SIMILARITY_THRESHOLD = 0.88
    MAX_DISTANCE_KM = 2.0

    @staticmethod
    def detect(complaint):

        candidates = IssueRepository.get_nearby(
            latitude=complaint.latitude,
            longitude=complaint.longitude,
            radius_km=DuplicateDetector.MAX_DISTANCE_KM
        )

        if not candidates:
            return None

        complaint_embedding = EmbeddingService.generate(
            f"{complaint.title}\n{complaint.description}"
        )

        if not complaint_embedding:
            return None

        vectors = []
        issue_ids = []

        for issue in candidates:
            if issue.embedding:
                vectors.append(issue.embedding)
                issue_ids.append(issue.id)

        if not vectors:
            return None

        index = faiss.IndexFlatIP(
            len(complaint_embedding)
        )

        embeddings = np.asarray(
            vectors,
            dtype=np.float32
        )

        faiss.normalize_L2(embeddings)
        index.add(embeddings)

        query = np.asarray(
            [complaint_embedding],
            dtype=np.float32
        )

        faiss.normalize_L2(query)

        scores, indices = index.search(query, 1)

        similarity = float(scores[0][0])

        if similarity >= DuplicateDetector.SIMILARITY_THRESHOLD:
            return {
                "issue": next(
                    issue for issue in candidates
                    if issue.id == issue_ids[indices[0][0]]
                ),
                "similarity_score": similarity
            }

        return None