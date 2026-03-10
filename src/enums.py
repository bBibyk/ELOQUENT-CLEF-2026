from enum import Enum
from typing import List

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
    MISTRAL_AI = "mistralAI"
    GROQ = "groq"