import os
from groq import Groq
from typing import Optional

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_llm(prompt: str, retries: int = 2) -> str:
    """
    Calls the LLM with basic retry and safety checks.
    Returns a non-empty string or an empty string on failure.
    """

    for attempt in range(retries + 1):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
            )

            content: Optional[str] = (
                response.choices[0].message.content
                if response and response.choices
                else None
            )

            if content and content.strip():
                return content.strip()

        except Exception:
            if attempt == retries:
                return ""

    return ""
