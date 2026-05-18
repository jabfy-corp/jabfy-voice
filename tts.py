import pyttsx3

_engine: pyttsx3.Engine | None = None


def _get_engine() -> pyttsx3.Engine:
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty("rate", 160)
    return _engine


def speak(text: str) -> None:
    engine = _get_engine()
    engine.say(text)
    engine.runAndWait()
