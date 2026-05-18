import io
from faster_whisper import WhisperModel

_model: WhisperModel | None = None


def _get_model() -> WhisperModel:
    global _model
    if _model is None:
        _model = WhisperModel("base", device="cpu", compute_type="int8")
    return _model


def transcribe(audio_bytes: bytes) -> str:
    model = _get_model()
    segments, _ = model.transcribe(io.BytesIO(audio_bytes), language="fr")
    return " ".join(s.text.strip() for s in segments).strip()
