import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

def ollama_generate(prompt: str, model: str = "llama3") -> str:
    """
    Minimal Ollama generate call.
    Replace model with whatever you run locally (llama3, mistral, etc.).
    """
    r = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=60,
    )
    r.raise_for_status()
    return r.json().get("response", "").strip()

def main():
    prompt = "Draft a short plan for building a simple API service in Python."
    draft = ollama_generate(prompt)
    print("\n=== LOCAL DRAFT ===\n")
    print(draft)

    print("\n=== NEXT STEPS ===\n")
    print("Add a cloud adapter + audit step to complete the workflow.")

if __name__ == "__main__":
    main()
