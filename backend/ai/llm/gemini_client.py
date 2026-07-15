from google import genai

from config.settings import Settings


class GeminiClient:

    client = genai.Client(
        api_key=Settings.GEMINI_API_KEY
    )