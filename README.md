# jabfy-voice

Voice input package for Jabfy. Handles microphone capture, speech-to-text transcription via Whisper, LLM responses via Ollama, and text-to-speech output via pyttsx3.

---

## Features

- Real-time microphone capture with automatic silence detection
- Local speech-to-text transcription using `faster-whisper`
- Conversational AI responses via Ollama (`llama3.2` by default)
- Text-to-speech voice output using `pyttsx3`
- Fully offline — no internet connection required after installation

---

## Architecture

```
Microphone
    │
    ▼
mic.py          — records audio until silence is detected
    │
    ▼
stt.py          — transcribes audio bytes to text (faster-whisper)
    │
    ▼
llm.py          — sends text to Ollama, returns LLM response
    │
    ▼
tts.py          — reads the response aloud (pyttsx3)
```

`main.py` ties all modules together in a continuous loop.

---

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running locally
- A working microphone

---

## Installation

**1. Clone the repository**

```bash
git clone git@github.com:jabfy-corp/jabfy-voice.git
cd jabfy-voice
```

**2. Install Python dependencies**

```bash
pip install -r requirements.txt
```

> On Linux, if `pyaudio` fails to install:
> ```bash
> sudo apt install portaudio19-dev
> pip install pyaudio
> ```

**3. Pull the Ollama model**

```bash
ollama pull llama3.2
```

Make sure the Ollama daemon is running:

```bash
ollama serve
```

---

## Usage

```bash
python3 main.py
```

The assistant will start listening immediately. Speak your question — it will stop recording automatically after a moment of silence, transcribe your speech, query Ollama, and read the answer aloud.

Press `Ctrl+C` to exit.

---

## File Reference

| File | Role |
|---|---|
| `main.py` | Entry point — runs the voice loop |
| `mic.py` | Records audio from the microphone until silence |
| `stt.py` | Transcribes audio bytes to text using `faster-whisper` |
| `llm.py` | Sends transcribed text to Ollama and returns the reply |
| `tts.py` | Converts the reply to speech using `pyttsx3` |
| `requirements.txt` | Python dependencies |

---

## Configuration

### Change the Ollama model

Edit `llm.py`, line 3:

```python
MODEL = "llama3.2"  # replace with any model pulled via ollama
```

Any model available via `ollama list` can be used (e.g. `mistral`, `llama3.1:8b`, `gemma3`).

### Change the transcription language

Edit `stt.py`, line 13:

```python
segments, _ = model.transcribe(io.BytesIO(audio_bytes), language="fr")
```

Replace `"fr"` with any [Whisper-supported language code](https://github.com/openai/whisper#available-models-and-languages).

### Change the speech rate

Edit `tts.py`, line 10:

```python
_engine.setProperty("rate", 160)  # words per minute
```

### Adjust silence detection sensitivity

Edit `mic.py`:

```python
SILENCE_THRESHOLD = 500   # lower = more sensitive
SILENCE_CHUNKS = 30       # number of silent chunks before stopping (~1.9s)
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `faster-whisper` | Local speech-to-text transcription |
| `pyaudio` | Microphone input stream |
| `ollama` | Python client for the Ollama API |
| `pyttsx3` | Local text-to-speech engine |

---

## Responsibilities in the Jabfy ecosystem

This package is responsible for:

- Wake word detection *(planned)*
- Microphone stream capture
- Speech-to-text transcription
- Feeding transcribed text to `jabfy-core` *(planned)*

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
