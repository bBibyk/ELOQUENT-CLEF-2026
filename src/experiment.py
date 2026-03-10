from src import enums
from src.models import abstract_model

import time
import random
import string

class Experiment:
    def __init__(self, model_choice : enums.Model, languages : set[enums.LanguageCode], specific : bool = False,
                 do_sample : bool = False, temprature : int = 0, system_prompt : str = "",
                 prefix : str = "", suffix : str = "", experiment_title : str = ""):
        self.languages = languages
        self.specific = specific
        self.experiment_title = experiment_title        
        self._model : abstract_model.AbstractModel = model_choice.to_model_class()(system_prompt=system_prompt, do_sample=do_sample, prefix=prefix, suffix=suffix, temperature=temprature)
        

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