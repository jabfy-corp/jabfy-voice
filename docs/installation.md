# Installation et lancement

## Prérequis

- **Python 3.10 à 3.12.** Python 3.13 ne convient pas : le module `audioop`, utilisé pour détecter le silence, y a été retiré.
- **Ollama** installé et démarré, avec le modèle `llama3.2`.
- **Un micro** et une sortie audio.
- **Sous Linux** : PortAudio pour `pyaudio`, et eSpeak pour `pyttsx3`.

```bash
sudo apt install portaudio19-dev espeak-ng   # Debian / Ubuntu
```

## Installation

```bash
git clone git@github.com:jabfy-corp/jabfy-voice.git
cd jabfy-voice
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ollama pull llama3.2
```

Au premier lancement, faster-whisper télécharge le modèle de transcription `base`. Ensuite, tout fonctionne hors ligne.

## Lancement

**En terminal** :

```bash
python3 main.py
```

L'assistant écoute tout de suite. Parle : l'enregistrement s'arrête après environ 1,9 seconde de silence, puis la question et la réponse s'affichent, et la réponse est lue à voix haute. `Ctrl+C` pour quitter.

**Avec l'interface web de suivi** :

```bash
python3 server.py
```

La même boucle tourne en arrière-plan, et la page `http://127.0.0.1:5000` affiche la conversation et l'état de l'assistant (écoute, réflexion, parole).

> Le serveur écoute sur toutes les interfaces réseau (`0.0.0.0`) : sur un réseau partagé, n'importe qui peut lire la conversation. Voir les [limites connues](README.md).

## Réglages

Il n'y a pas encore de fichier de configuration : les réglages sont des constantes dans le code.

| Réglage | Fichier | Valeur actuelle |
|---|---|---|
| Modèle de langage | `llm.py`, `MODEL` | `llama3.2` (tout modèle de `ollama list`) |
| Modèle de transcription | `stt.py`, `WhisperModel(...)` | `base`, CPU, `int8` |
| Langue de transcription | `stt.py`, `language=` | `fr` |
| Seuil de détection de voix | `mic.py`, `SILENCE_THRESHOLD` | `500` (plus bas = plus sensible) |
| Durée de silence de fin | `mic.py`, `SILENCE_CHUNKS` | `30` blocs, soit environ 1,9 s |
| Débit de la voix | `tts.py`, `rate` | `160` mots par minute |

## Dépannage

| Problème | Cause probable |
|---|---|
| `ModuleNotFoundError: No module named 'audioop'` | Python 3.13 ou plus récent : utiliser Python 3.12 |
| `pyaudio` ne s'installe pas | PortAudio manquant : `sudo apt install portaudio19-dev` |
| Aucune voix sous Linux | eSpeak manquant : `sudo apt install espeak-ng` |
| `ollama._types.ResponseError` ou connexion refusée | Ollama n'est pas démarré (`ollama serve`) ou le modèle n'est pas téléchargé |
| L'enregistrement ne s'arrête jamais | Bruit de fond au-dessus du seuil : augmenter `SILENCE_THRESHOLD` |
