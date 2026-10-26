"""Phase 5 starter: your first LLM API call, then structured output.

Setup:
    pip install -r requirements-llm.txt
    cp .env.example .env     # add your ANTHROPIC_API_KEY
Run:
    python phase-5-llm-apis/first_call.py
"""

import json
import os

import anthropic
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY from the environment
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5")


def ask(prompt: str, system: str = "You are a concise, helpful assistant.") -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    print(f"[tokens in={response.usage.input_tokens} out={response.usage.output_tokens}]")
    return response.content[0].text


def triage(ticket: str) -> dict:
    """Ask for JSON, then validate it in code. Never trust the format blindly."""
    system = (
        "You classify support tickets. Reply with JSON only, no other text, using exactly "
        'these keys: "category" (one of billing, login, device, sync, other), '
        '"priority" (low, medium, high), "summary" (max 15 words).'
    )
    raw = ask(f"<ticket>\n{ticket}\n</ticket>", system=system)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Model did not return valid JSON: {raw!r}") from exc

    allowed = {"billing", "login", "device", "sync", "other"}
    if data.get("category") not in allowed:
        raise ValueError(f"Unexpected category: {data.get('category')!r}")
    return data


if __name__ == "__main__":
    print(ask("Explain what an API is in two sentences."))
    print()
    print(triage("I was charged twice this month and nobody has replied to my email!"))

    # ------------------------------------------------------------------
    # YOUR TURN:
    # 1. Print response.stop_reason. What does it tell you?
    # 2. Make triage() retry once if the JSON is invalid, then give up cleanly.
    # 3. Replace the manual checks with a Pydantic model for validation.
    # 4. Feed triage() a ticket that contains "ignore previous instructions and ...".
    #    What happens? How could you make the system more robust?
    # 5. Write a pytest test for triage() that mocks `ask` so no real API call is made.
    # ------------------------------------------------------------------
