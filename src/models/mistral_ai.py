import os
from src.models.abstract_model import AbstractModel
from mistralai.client import Mistral

def _get_model():
    api_key = os.environ.get("MISTRAL_API_KEY")
    client = Mistral(api_key=api_key)
    return client

def _generate(client, model_name: str, user_input: str, system_prompt: str, prefix: str, suffix: str, temperature: float) -> str:
    prompt = f"{prefix}\n{user_input}\n{suffix}"
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    response = client.chat.complete(
        model=model_name,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

class MistralBaseModel(AbstractModel):
    """Classe de base factorisée pour les modèles Mistral."""
    model_name: str = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_client = _get_model()
    
    def generate(self, user_input: str) -> str:
        return _generate(self.model_client, self.model_name, user_input, self.system_prompt, self.prefix, self.suffix, self.temperature)

class MistralNeMo(MistralBaseModel): model_name = "open-mistral-nemo"
class MistralLarge(MistralBaseModel): model_name = "mistral-large-latest"