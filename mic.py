import io
import wave
import pyaudio

RATE = 16000
CHANNELS = 1
CHUNK = 1024
FORMAT = pyaudio.paInt16
SILENCE_THRESHOLD = 500
SILENCE_CHUNKS = 30  # ~1.9s of silence ends recording


def _rms(data: bytes) -> float:
    import audioop
    return audioop.rms(data, 2)


def record_until_silence() -> bytes:
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )

    print("Écoute... (parle, silence pour terminer)")
    frames = []
    silent_count = 0
    started = False

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        level = _rms(data)

        if level > SILENCE_THRESHOLD:
            started = True
            silent_count = 0
            frames.append(data)
        elif started:
            frames.append(data)
            silent_count += 1
            if silent_count >= SILENCE_CHUNKS:
                break

    stream.stop_stream()
    stream.close()
    pa.terminate()

    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(pa.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

    return buf.getvalue()
