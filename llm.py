import os
import ollama

MODEL = os.getenv("JABFY_VOICE_MODEL", "llama3.2")
_client = ollama.Client(host=os.getenv("OLLAMA_HOST", "http://localhost:11434"))
_history: list[dict] = []


def ask(user_text: str) -> str:
    _history.append({"role": "user", "content": user_text})
    response = _client.chat(model=MODEL, messages=_history)
    reply = response["message"]["content"]
    _history.append({"role": "assistant", "content": reply})
    return reply


def reset_history() -> None:
    _history.clear()
