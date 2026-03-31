from abc import ABC, abstractmethod

class AbstractModel(ABC):
    model_name : str
    def __init__(self, 
                 system_prompt: str = "", 
                 prefix: str = "", 
                 suffix: str = "", 
                 do_sample: bool = False, 
                 temperature: float = 0.0):
        self.system_prompt = system_prompt
        self.prefix = prefix
        self.suffix = suffix
        self.do_sample = do_sample
        self.temperature = temperature
        self.model_client = None

    def get_model_name(self) -> str:
        return self.model_name

    @abstractmethod
    def generate(self, user_input: str) -> str:
        """
        user_input : la donnée brute (ex: une phrase à traduire).
        La méthode peut combiner prefix + user_input + suffix.
        """
        raise NotImplementedError("La méthode generate doit être implémentée.")