import threading
from flask import Flask, render_template, jsonify
from mic import record_until_silence
from stt import transcribe
from llm import ask
from tts import speak

app = Flask(__name__)

_state = {
    "messages": [],
    "status": "idle",  # idle | listening | thinking | speaking
}
_lock = threading.Lock()


def _set_status(s: str) -> None:
    with _lock:
        _state["status"] = s


def _add_message(role: str, text: str) -> None:
    with _lock:
        _state["messages"].append({"role": role, "text": text})


def _voice_loop() -> None:
    while True:
        _set_status("listening")
        audio = record_until_silence()

        _set_status("thinking")
        question = transcribe(audio)
        if not question:
            _set_status("idle")
            continue

        _add_message("user", question)
        answer = ask(question)
        _add_message("assistant", answer)

        _set_status("speaking")
        speak(answer)
        _set_status("idle")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/state")
def state():
    with _lock:
        return jsonify(_state)


if __name__ == "__main__":
    t = threading.Thread(target=_voice_loop, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=5000, debug=False)
