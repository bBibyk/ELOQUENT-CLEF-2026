from src import enums
from src.models import abstract_model
import pandas as pd
import datetime
import json
import os
import time

from dotenv import load_dotenv
load_dotenv()

class Experiment:
    def __init__(self, model_choice : enums.Model, languages : set[enums.LanguageCode], specific : bool = False,
                 do_sample : bool = False, temprature : int = 0, system_prompt : str = "",
                 prefix : str = "", suffix : str = "", experiment_title : str = "",
                 start_line : int = 0, end_line : int = None):
        self._languages = languages
        self._specific = specific
        self._experiment_title = experiment_title
        self._model_choice = model_choice
        self._result_df = pd.DataFrame(columns=["id", "prompt", "answer"])
        self._start_line = start_line
        self._end_line = end_line
        
        self._model : abstract_model.AbstractModel = model_choice.to_model_class()(system_prompt=system_prompt, do_sample=do_sample, prefix=prefix, suffix=suffix, temperature=temprature)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        model_id = self._model_choice.value.replace(" ", "_").lower()
        self._output_dir = os.path.join("data", "output", f"{model_id}_{timestamp}")
        os.makedirs(self._output_dir, exist_ok=True)
        
    
    def _save_experiment_footprint(self):
        footprint_path = os.path.join(self._output_dir, "submission_metadata.json")

        footprint = {
            "team": "Nabil Ebalo",
            "system": "eloquent-system",
            "model": self._model_choice.value,
            "submissionid": self._experiment_title or "experiment-1",
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "label": "eloquent-2026-cultural",
            "languages": [lang.value for lang in self._languages],
            "modifications": {
                "system_prompt": self._model.system_prompt,
                "prompt_prefix_english": self._model.prefix,
                "prompt_suffix_english": self._model.suffix,
                "generation_params": {
                    "do_sample": self._model.do_sample,
                    "temperature": self._model.temperature
                },
                "notes": f"Experiment specific: {self._specific}. Title: {self._experiment_title}"
            }
        }

        with open(footprint_path, "w", encoding="utf-8") as f:
            json.dump(footprint, f, indent=4, ensure_ascii=False)

    def run(self):
        """
        Générateur qui produit les résultats intermédiaires
        """
        speceficity = "specific"
        if not self._specific:
            speceficity = "un" + speceficity
        for language in self._languages:
            df = pd.read_json(f"data/input/{language.value}_{speceficity}.jsonl", lines=True)
            self._save_experiment_footprint()
            
            curr_end = self._end_line if self._end_line is not None else len(df)
            df_subset = df.iloc[self._start_line : curr_end]
            
            for id, row in df_subset.iterrows():
                prompt_text = row['prompt']
                result = self._model.generate(prompt_text)
                self._result_df.loc[id] = [id, prompt_text, result]
                self._result_df.to_json(f"{self._output_dir}/{language.value}_{speceficity}.jsonl", orient="records", lines=True, force_ascii=False)
                time.sleep(0.5)
                yield prompt_text, result





if __name__=="__main__":
    print("ok")