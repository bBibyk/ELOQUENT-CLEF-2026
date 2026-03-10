from abc import ABC, abstractmethod

class AbstractModel(ABC):
    @abstractmethod
    def predict(self, data: str) -> str:
        """Chaque modèle devra implémenter cette méthode."""
        pass