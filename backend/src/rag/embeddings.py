import requests

OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"   # Modelo gratis de Ollama


def generate_embedding(text: str):
    """Genera embeddings usando Ollama de forma local y gratuita."""
    payload = {
        "model": EMBED_MODEL,
        "prompt": text
    }

    response = requests.post(OLLAMA_EMBED_URL, json=payload)

    if response.status_code != 200:
        raise Exception(f"Error generating embedding: {response.text}")

    vector = response.json().get("embedding")

    return vector
