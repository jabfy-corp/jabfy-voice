# Interfaces

## Fonctions des modules

Chaque étape est une fonction simple, réutilisable séparément :

| Fonction | Entrée | Sortie |
|---|---|---|
| `mic.record_until_silence()` | — | `bytes` : fichier WAV, 16 kHz, mono, 16 bits |
| `stt.transcribe(audio_bytes)` | `bytes` WAV | `str` : texte transcrit, vide si rien n'a été compris |
| `llm.ask(user_text)` | `str` | `str` : réponse du modèle, ajoutée à l'historique |
| `llm.reset_history()` | — | vide l'historique de la conversation |
| `tts.speak(text)` | `str` | lit le texte à voix haute et rend la main à la fin de la lecture |

## API HTTP de l'interface web

Lancée par `python3 server.py`, sur le port `5000`. Elle est en **lecture seule** : on ne peut ni envoyer de question ni piloter l'assistant par HTTP.

| Méthode et chemin | Réponse |
|---|---|
| `GET /` | Page web de suivi de la conversation |
| `GET /state` | État courant, en JSON |

Exemple de réponse de `GET /state` :

```json
{
  "status": "speaking",
  "messages": [
    { "role": "user", "text": "Quelle température fait-il dans le salon ?" },
    { "role": "assistant", "text": "Je n'ai pas accès aux capteurs de la maison pour l'instant." }
  ]
}
```

`status` vaut `idle`, `listening`, `thinking` ou `speaking`.

## Dépendances externes

| Dépendance | Utilisée par | Rôle |
|---|---|---|
| Ollama (API locale, port 11434 par défaut) | `llm.py` | Génération des réponses, modèle `llama3.2` |
| faster-whisper | `stt.py` | Transcription |
| PortAudio, via `pyaudio` | `mic.py` | Accès au micro |
| Moteur vocal du système, via `pyttsx3` | `tts.py` | Synthèse vocale |
| Flask | `server.py` | Interface web |

## Ce qui est prévu

Pour s'intégrer à Jabfy, jabfy-voice devra envoyer la transcription à jabfy-core au lieu d'Ollama, et lire la réponse que Core renvoie. Le contrat n'est pas encore défini : voir la page Architecture › Flux d'une demande de jabfy-docs.
