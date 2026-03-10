from abc import ABC, abstractmethod

class AbstractModel(ABC):
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

    @abstractmethod
    def generate(self, user_input: str) -> str:
        """
        user_input : la donnée brute (ex: une phrase à traduire).
        La méthode doit combiner prefix + user_input + suffix.
        """
        pass