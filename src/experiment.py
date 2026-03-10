from src import enums
from src.models import abstract_model

import time
import random
import string

class Experiment:
    def __init__(self, model_choice : enums.Model, languages : set[enums.LanguageCode], do_sample : bool = False, temprature : int = 0,
                 system_promp : str = "", prefix : str = "", suffix : str = "", title : str = ""):
        self._model : abstract_model.AbstractModel = model_choice.to_model()
        self.title = title
        self.languages = languages
        self.do_sample = do_sample
        self.temprature = temprature

    def run(self):
        """
        Générateur qui produit les résultats intermédiaires
        """
        for i in range(1, 11):
            random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            result = f"Pass {i}/10 - Modèle: {self.title} - Data: {random_str}"
            yield result
            time.sleep(1)





if __name__=="__main__":
    print("ok")