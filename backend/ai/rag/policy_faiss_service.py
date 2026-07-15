import os

import faiss
import numpy as np


class PolicyFaissService:

    DIMENSION = 3072

    STORAGE_DIR = "storage"

    INDEX_FILE = os.path.join(
        STORAGE_DIR,
        "policy.index"
    )

    index = None

    @classmethod
    def initialize(cls):

        os.makedirs(
            cls.STORAGE_DIR,
            exist_ok=True
        )

        if os.path.exists(
            cls.INDEX_FILE
        ):

            cls.index = faiss.read_index(
                cls.INDEX_FILE
            )

        else:

            cls.index = faiss.IndexFlatIP(
                cls.DIMENSION
            )

    @classmethod
    def exists(cls):

        return os.path.exists(
            cls.INDEX_FILE
        )

    @classmethod
    def add(
        cls,
        embedding: list[float]
    ):

        vector = np.array(
            [embedding],
            dtype=np.float32
        )

        faiss.normalize_L2(
            vector
        )

        cls.index.add(
            vector
        )

    @classmethod
    def save(cls):

        faiss.write_index(
            cls.index,
            cls.INDEX_FILE
        )

    @classmethod
    def search(
        cls,
        embedding: list[float],
        k: int = 5
    ):

        if cls.index.ntotal == 0:

            return [], []

        vector = np.array(
            [embedding],
            dtype=np.float32
        )

        faiss.normalize_L2(
            vector
        )

        scores, indices = cls.index.search(
            vector,
            min(
                k,
                cls.index.ntotal
            )
        )

        return (
            scores[0].tolist(),
            indices[0].tolist()
        )

    @classmethod
    def total_vectors(cls):

        return cls.index.ntotal