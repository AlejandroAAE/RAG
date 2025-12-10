import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
LLM_MODEL = "llama3.1"   # Puedes usar qwen2.5 si quieres


def ask_llm(prompt: str) -> str:
    """Envía un prompt al modelo local de Ollama."""
    payload = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        raise Exception(f"Error calling LLM: {response.text}")

    return response.json().get("response")
