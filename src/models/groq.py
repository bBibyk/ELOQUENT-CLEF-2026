import os
from src.models.abstract_model import AbstractModel
from groq import Groq

def _get_model(model_name: str, system_prompt: str):
    key = os.environ.get("GROQ_API_KEY")
    client = Groq(api_key=key)
    return client

def _generate(client, model_name: str, user_input: str, system_prompt: str, prefix: str, suffix: str, temperature: float) -> str:
    prompt = f"{prefix}\n{user_input}\n{suffix}"
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

class GroqBaseModel(AbstractModel):
    """Classe de base factorisée pour les modèles Groq."""
    model_name: str = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_client = _get_model(self.model_name, self.system_prompt)
    
    def generate(self, user_input: str) -> str:
        return _generate(self.model_client, self.model_name, user_input, self.system_prompt, self.prefix, self.suffix, self.temperature)

class Lama4Scout(GroqBaseModel): model_name = "meta-llama/llama-4-scout-17b-16e-instruct"
class KimiK2(GroqBaseModel): model_name = "moonshotai/kimi-k2-instruct-0905"
class Llama31_8B(GroqBaseModel): model_name = "llama-3.1-8b-instant"
