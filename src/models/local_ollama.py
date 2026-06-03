import os
import ollama
from src.models.abstract_model import AbstractModel

class OllamaBaseModel(AbstractModel):
    """Classe de base pour les modèles exécutés localement via Ollama."""
    model_name: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # L'adresse de l'hôte Ollama peut être configurée via la variable d'environnement OLLAMA_HOST
        host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        self.model_client = ollama.Client(host=host)

    def generate(self, user_input: str) -> str:
        prompt = f"{self.prefix}\n{user_input}\n{self.suffix}"
        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        messages.append({"role": "user", "content": prompt})

        # Options de génération pour Ollama
        options = {
            "temperature": self.temperature,
            "num_predict": self.max_new_tokens
        }

        response = self.model_client.chat(
            model=self.model_name,
            messages=messages,
            options=options
        )
        return response['message']['content']

class MistralNeMoLocal(OllamaBaseModel):
    model_name = "mistral-nemo"

class Llama31_8BLocal(OllamaBaseModel):
    model_name = "llama3.1"

class Gemma31bItLocal(OllamaBaseModel):
    model_name = "gemma3:1b"

class Gemma34bItLocal(OllamaBaseModel):
    model_name = "gemma3:4b"

class Gemma312bItLocal(OllamaBaseModel):
    model_name = "gemma3:12b"

class Gemma327bItLocal(OllamaBaseModel):
    model_name = "gemma3:27b"

class Gemma3nE4bItLocal(OllamaBaseModel):
    model_name = "gemma3n:4b"

class Gemma3nE2bItLocal(OllamaBaseModel):
    model_name = "gemma3n:2b"
