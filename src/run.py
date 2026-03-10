import enums

class Run:
    def __init__(self, model : enums.Model, languages : set[enums.LanguageCode], temprature : int,
                 system_promp : str = "", prefix : str = "", suffix : str = "", title : str = ""):
        self._model = model
