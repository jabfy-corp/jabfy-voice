from mic import record_until_silence
from stt import transcribe
from llm import ask
from tts import speak


def run() -> None:
    print("Assistant vocal démarré. Ctrl+C pour quitter.\n")
    while True:
        audio = record_until_silence()
        question = transcribe(audio)
        if not question:
            continue
        print(f"Vous : {question}")
        answer = ask(question)
        print(f"Assistant : {answer}\n")
        speak(answer)


if __name__ == "__main__":
    run()
