import ollama

MODEL = "llama3.2"
_history: list[dict] = []


def ask(user_text: str) -> str:
    _history.append({"role": "user", "content": user_text})
    response = ollama.chat(model=MODEL, messages=_history)
    reply = response["message"]["content"]
    _history.append({"role": "assistant", "content": reply})
    return reply


def reset_history() -> None:
    _history.clear()
