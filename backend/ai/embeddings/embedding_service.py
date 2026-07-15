import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[2]))
    from ai.llm.gemini_client import GeminiClient
else:
    from ai.llm.gemini_client import GeminiClient



class EmbeddingService:

    MODEL = "gemini-embedding-001"

    @staticmethod
    def generate(
        text: str
    ) -> list[float]:

        response = GeminiClient.client.models.embed_content(
            model=EmbeddingService.MODEL,
            contents=text
        )

        return response.embeddings[0].values