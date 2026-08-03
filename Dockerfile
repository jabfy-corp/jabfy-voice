FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    JABFY_VOICE_ENABLE_AUDIO=false \
    OLLAMA_HOST=http://host.docker.internal:11434

WORKDIR /app

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential \
        espeak-ng \
        ffmpeg \
        portaudio19-dev \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid 10001 jabfy \
    && useradd --create-home --uid 10001 --gid jabfy jabfy

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER jabfy

EXPOSE 5000

CMD ["python", "server.py"]

