import os
from src.models.abstract_model import AbstractModel
import google.generativeai as genai

def _get_model(model_name: str, system_prompt: str):
    key = os.environ.get("GOOGLE_API_KEY")
    genai.configure(api_key=key)
    if system_prompt:
        return genai.GenerativeModel(system_instruction=system_prompt, model_name=model_name)
    else:
        return genai.GenerativeModel(model_name=model_name)

def _generate(model, user_input: str, prefix: str, suffix: str, temperature: float, max_new_tokens: int) -> str:
    prompt = f"{prefix}\n{user_input}\n{suffix}"
    generation_config = genai.types.GenerationConfig(temperature=temperature, max_output_tokens=max_new_tokens)
    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text

class GoogleBaseModel(AbstractModel):
    """Classe de base factorisée pour les modèles Google."""
    model_name: str = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_client = _get_model(self.model_name, self.system_prompt)
    
    def generate(self, user_input: str) -> str:
        return _generate(self.model_client, user_input, self.prefix, self.suffix, self.temperature, self.max_new_tokens)

class Gemini25Flash(GoogleBaseModel): model_name = "gemini-2.5-flash"
class Gemini25Pro(GoogleBaseModel): model_name = "gemini-2.5-pro"
class Gemini20Flash(GoogleBaseModel): model_name = "gemini-2.0-flash"
class Gemini20Flash001(GoogleBaseModel): model_name = "gemini-2.0-flash-001"
class Gemini20FlashLite001(GoogleBaseModel): model_name = "gemini-2.0-flash-lite-001"
class Gemini20FlashLite(GoogleBaseModel): model_name = "gemini-2.0-flash-lite"
class Gemma31bIt(GoogleBaseModel): model_name = "gemma-3-1b-it"
class Gemma34bIt(GoogleBaseModel): model_name = "gemma-3-4b-it"
class Gemma312bIt(GoogleBaseModel): model_name = "gemma-3-12b-it"
class Gemma327bIt(GoogleBaseModel): model_name = "gemma-3-27b-it"
class Gemma3nE4bIt(GoogleBaseModel): model_name = "gemma-3n-e4b-it"
class Gemma3nE2bIt(GoogleBaseModel): model_name = "gemma-3n-e2b-it"
class GeminiFlashLatest(GoogleBaseModel): model_name = "gemini-flash-latest"
class GeminiFlashLiteLatest(GoogleBaseModel): model_name = "gemini-flash-lite-latest"
class GeminiProLatest(GoogleBaseModel): model_name = "gemini-pro-latest"
class Gemini25FlashLite(GoogleBaseModel): model_name = "gemini-2.5-flash-lite"
class Gemini25FlashLitePreview092025(GoogleBaseModel): model_name = "gemini-2.5-flash-lite-preview-09-2025"
class Gemini3ProPreview(GoogleBaseModel): model_name = "gemini-3-pro-preview"
class Gemini3FlashPreview(GoogleBaseModel): model_name = "gemini-3-flash-preview"
class Gemini31ProPreview(GoogleBaseModel): model_name = "gemini-3.1-pro-preview"
class Gemini31ProPreviewCustomtools(GoogleBaseModel): model_name = "gemini-3.1-pro-preview-customtools"
class Gemini31FlashLitePreview(GoogleBaseModel): model_name = "gemini-3.1-flash-lite-preview"
class NanoBananaProPreview(GoogleBaseModel): model_name = "nano-banana-pro-preview"
class DeepResearchProPreview122025(GoogleBaseModel): model_name = "deep-research-pro-preview-12-2025"