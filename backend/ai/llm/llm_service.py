import json
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[2]))
    from ai.llm.gemini_client import GeminiClient
else:
    from ai.llm.gemini_client import GeminiClient

class LLMService:

    MODEL = "gemini-3.5-flash"

    @staticmethod
    def analyze(
        title: str,
        description: str
    ) -> dict:

        prompt = f"""
You are an AI assistant for a municipal complaint management system.

Analyze the following complaint.

Title:
{title}

Description:
{description}

Your tasks are:

1. Identify the complaint category.

Possible Categories:
- Road Damage
- Water Leakage
- Drainage
- Street Light
- Garbage

2. Generate a concise summary (maximum 25 words).

3. Suggest the most relevant department name from this list:
- Roads
- Drainage
- Water Supply
- Street Light
- Waste Management

Return ONLY valid JSON.

Example:

{{
    "category": "Road",
    "summary": "Large pothole near the central bus stand causing traffic disruption.",
    "department": "Roads"
}}
"""

        response = GeminiClient.client.models.generate_content(
            model=LLMService.MODEL,
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace(
                "```json",
                ""
            )

            text = text.replace(
                "```",
                ""
            )

        elif text.startswith("```"):
            text = text.replace(
                "```",
                ""
            )

        return json.loads(text)