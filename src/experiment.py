import enums
from models import *

class Experiment:
    def __init__(self, model : enums.Model, languages : set[enums.LanguageCode], do_sample : bool = False, temprature : int = 0,
                 system_promp : str = "", prefix : str = "", suffix : str = "", title : str = ""):
        self._model : abstract_model.AbstractModel = model

    def run():







if __name__=="__main__":
    print("ok")