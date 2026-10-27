# Tests

## État actuel

Il n'y a **aucun test automatisé** : le dépôt n'a ni dossier `tests/`, ni CI qui lance des tests. La seule vérification possible est manuelle, avec un vrai micro et Ollama démarré.

## Vérification manuelle

1. Lancer `python3 main.py`.
2. Dire une phrase courte, par exemple « Bonjour, qui es-tu ? ».
3. Vérifier que la transcription affichée correspond à la phrase, qu'une réponse s'affiche, et qu'elle est lue à voix haute.
4. Relancer avec `python3 server.py` et vérifier que `http://127.0.0.1:5000` affiche la conversation et les changements d'état.

## Tests à écrire

Chaque étape étant une fonction indépendante, elle peut être testée sans micro ni modèle :

| Module | Test proposé |
|---|---|
| `mic.py` | Remplacer le flux PyAudio par de faux blocs audio : vérifier que l'enregistrement démarre au-dessus du seuil et s'arrête après 30 blocs silencieux. |
| `stt.py` | Transcrire un fichier WAV de référence en français, et mesurer le taux d'erreur (WER) sur un jeu de phrases : c'est aussi la métrique Performance › WER de jabfy-docs. |
| `llm.py` | Remplacer `ollama.chat` par une fausse fonction : vérifier que l'historique contient bien la question puis la réponse, et que `reset_history()` le vide. |
| `server.py` | Avec le client de test Flask : `GET /state` renvoie le bon format et les bons statuts. |

Ces tests tourneraient en CI sans matériel audio ni serveur Ollama.
