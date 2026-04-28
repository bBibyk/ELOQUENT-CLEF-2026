import os
from src.models.abstract_model import AbstractModel
from openai import OpenAI

def _get_model(model_name: str, system_prompt: str):
    key = os.environ.get("DEEPSEEK_API_KEY")
    client = OpenAI(api_key=key, base_url="https://api.deepseek.com")
    return client

def _generate(client, model_name: str, user_input: str, system_prompt: str, prefix: str, suffix: str, temperature: float, max_new_tokens: int) -> str:
    prompt = f"{prefix}\n{user_input}\n{suffix}"
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=temperature,
        max_tokens=max_new_tokens
    )
    return response.choices[0].message.content

class DeepSeekBaseModel(AbstractModel):
    """Classe de base factorisée pour les modèles DeepSeek."""
    model_name: str = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_client = _get_model(self.model_name, self.system_prompt)
    
    def generate(self, user_input: str) -> str:
        return _generate(self.model_client, self.model_name, user_input, self.system_prompt, self.prefix, self.suffix, self.temperature, self.max_new_tokens)

class DeepSeekChat(DeepSeekBaseModel): model_name = "deepseek-chat"
