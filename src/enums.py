from enum import Enum
from typing import List
from src.models import (abstract_model,
                    mistral_ai,
                    google,
                    groq,
                    deepseek,
                    )

class BaseEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def list_choices(cls) -> List[str]:
        """Retourne la liste des noms des membres de l'enum."""
        return [member.name for member in cls]
    
    @classmethod
    def list_values(cls) -> List[str]:
        """Retourne la liste des valeurs (le contenu) de l'enum."""
        return [str(member.value) for member in cls]
    
class LanguageCode(BaseEnum):
    BENGALI = "bn"
    CATALAN = "ca"
    CZECH = "cs"
    DANISH = "da"
    GERMAN = "de"
    GREEK = "el"
    ENGLISH = "en"
    SPANISH = "es"
    FINNISH = "fi"
    FAROESE = "fo"
    FRENCH = "fr"
    HEBREW = "he"
    HINDI = "hi"
    ITALIAN = "it"
    KANNADA = "kn"
    MARATHI = "mr"
    POLISH = "pl"
    RUSSIAN = "ru"
    SLOVAK = "sk"
    SWEDISH = "sv"
    TAMIL = "ta"
    TELUGU = "te"

class Model(BaseEnum):
    MISTRAL_LARGE = "Mistral Large"
    MISTRAL_NEMO = "Mistral NeMo"
    GEMINI_2_5_FLASH = "Gemini 2.5 Flash"
    # GEMINI_2_5_PRO = "Gemini 2.5 Pro"
    # GEMINI_2_0_FLASH = "Gemini 2.0 Flash"
    # GEMINI_2_0_FLASH_001 = "Gemini 2.0 Flash 001"
    # GEMINI_2_0_FLASH_LITE_001 = "Gemini 2.0 Flash Lite 001"
    # GEMINI_2_0_FLASH_LITE = "Gemini 2.0 Flash Lite"
    # GEMMA_3_1B_IT = "Gemma 3 1B IT"
    # GEMMA_3_4B_IT = "Gemma 3 4B IT"
    # GEMMA_3_12B_IT = "Gemma 3 12B IT"
    # GEMMA_3_27B_IT = "Gemma 3 27B IT"
    # GEMMA_3N_E4B_IT = "Gemma 3n E4B IT"
    # GEMMA_3N_E2B_IT = "Gemma 3n E2B IT"
    # GEMINI_FLASH_LATEST = "Gemini Flash Latest"
    # GEMINI_FLASH_LITE_LATEST = "Gemini Flash Lite Latest"
    # GEMINI_PRO_LATEST = "Gemini Pro Latest"
    # GEMINI_2_5_FLASH_LITE = "Gemini 2.5 Flash Lite"
    # GEMINI_2_5_FLASH_LITE_PREVIEW_09_2025 = "Gemini 2.5 Flash Lite Preview 09-2025"
    # GEMINI_3_PRO_PREVIEW = "Gemini 3 Pro Preview"
    # GEMINI_3_FLASH_PREVIEW = "Gemini 3 Flash Preview"
    # GEMINI_3_1_PRO_PREVIEW = "Gemini 3.1 Pro Preview"
    # GEMINI_3_1_PRO_PREVIEW_CUSTOMTOOLS = "Gemini 3.1 Pro Preview Customtools"
    GEMINI_3_1_FLASH_LITE_PREVIEW = "Gemini 3.1 Flash Lite Preview"
    LLAMA_3_1_8B = "Llama 3.1 (8B)"
    LAMA_4_SCOUT = "Lama 4 Scout"
    KIMI_K2 = "Kimi K2"
    DEEPSEEK_CHAT = "DeepSeek Chat"

    def to_model_class(self) -> type[abstract_model.AbstractModel]:
        if self.name=="MISTRAL_NEMO":
            return mistral_ai.MistralNeMo
        elif self.name=="MISTRAL_LARGE":
            return mistral_ai.MistralLarge
        elif self.name=="GEMINI_2_5_FLASH":
            return google.Gemini25Flash
        elif self.name=="GEMINI_1_5_FLASH":
            return google.Gemini15Flash
        elif self.name=="GEMINI_2_5_PRO":
            return google.Gemini25Pro
        elif self.name=="GEMINI_2_0_FLASH":
            return google.Gemini20Flash
        elif self.name=="GEMINI_2_0_FLASH_001":
            return google.Gemini20Flash001
        elif self.name=="GEMINI_2_0_FLASH_LITE_001":
            return google.Gemini20FlashLite001
        elif self.name=="GEMINI_2_0_FLASH_LITE":
            return google.Gemini20FlashLite
        elif self.name=="GEMMA_3_1B_IT":
            return google.Gemma31bIt
        elif self.name=="GEMMA_3_4B_IT":
            return google.Gemma34bIt
        elif self.name=="GEMMA_3_12B_IT":
            return google.Gemma312bIt
        elif self.name=="GEMMA_3_27B_IT":
            return google.Gemma327bIt
        elif self.name=="GEMMA_3N_E4B_IT":
            return google.Gemma3nE4bIt
        elif self.name=="GEMMA_3N_E2B_IT":
            return google.Gemma3nE2bIt
        elif self.name=="GEMINI_FLASH_LATEST":
            return google.GeminiFlashLatest
        elif self.name=="GEMINI_FLASH_LITE_LATEST":
            return google.GeminiFlashLiteLatest
        elif self.name=="GEMINI_PRO_LATEST":
            return google.GeminiProLatest
        elif self.name=="GEMINI_2_5_FLASH_LITE":
            return google.Gemini25FlashLite
        elif self.name=="GEMINI_2_5_FLASH_LITE_PREVIEW_09_2025":
            return google.Gemini25FlashLitePreview092025
        elif self.name=="GEMINI_3_PRO_PREVIEW":
            return google.Gemini3ProPreview
        elif self.name=="GEMINI_3_FLASH_PREVIEW":
            return google.Gemini3FlashPreview
        elif self.name=="GEMINI_3_1_PRO_PREVIEW":
            return google.Gemini31ProPreview
        elif self.name=="GEMINI_3_1_PRO_PREVIEW_CUSTOMTOOLS":
            return google.Gemini31ProPreviewCustomtools
        elif self.name=="GEMINI_3_1_FLASH_LITE_PREVIEW":
            return google.Gemini31FlashLitePreview
        elif self.name=="LAMA_4_SCOUT":
            return groq.Lama4Scout
        elif self.name=="LLAMA_3_1_8B":
            return groq.Llama31_8B
        elif self.name=="KIMI_K2":
            return groq.KimiK2
        elif self.name=="DEEPSEEK_CHAT":
            return deepseek.DeepSeekChat