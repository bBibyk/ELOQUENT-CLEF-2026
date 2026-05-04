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
    def __init__(
        self,
        model_choice: enums.Model,
        languages: set[enums.LanguageCode],
        specific: bool = False,
        do_sample: bool = False,
        temprature: int = 0,
        system_prompt: str = "",
        prefix: str = "",
        suffix: str = "",
        experiment_title: str = "",
        start_line: int = 0,
        end_line: int = None,
        max_new_tokens: int = 200,
    ):
        self._languages = languages
        self._specific = specific
        self._experiment_title = experiment_title
        self._model_choice = model_choice
        self._result_df = pd.DataFrame(columns=["id", "prompt", "answer"])
        self._start_line = start_line
        self._end_line = end_line

        self._model: abstract_model.AbstractModel = model_choice.to_model_class()(
            system_prompt=system_prompt,
            do_sample=do_sample,
            prefix=prefix,
            suffix=suffix,
            temperature=temprature,
            max_new_tokens=max_new_tokens,
        )

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        model_id = self._model_choice.value.replace(" ", "_").lower()
        self._output_dir = os.path.join("data", "output", f"{model_id}_{timestamp}")
        os.makedirs(self._output_dir, exist_ok=True)

    def _save_experiment_footprint(self):
        footprint_path = os.path.join(self._output_dir, "submission_metadata.json")

        footprint = {
            "team": "TtlySpicy",
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
                    "temperature": self._model.temperature,
                    "max_new_tokens": self._model.max_new_tokens,
                },
                "notes": f"Experiment specific: {self._specific}. Title: {self._experiment_title}",
            },
        }

        with open(footprint_path, "w", encoding="utf-8") as f:
            json.dump(footprint, f, indent=4, ensure_ascii=False)

    def run(self):
        """
        Générateur qui produit les résultats intermédiaires avec gestion des limites API.
        """
        speceficity = "specific" if self._specific else "unspecific"
        
        for language in self._languages:
            df = pd.read_json(
                f"data/input/{language.value}_{speceficity}.jsonl", lines=True
            )
            self._save_experiment_footprint()

            if self._end_line is not None:
                df_subset = df.iloc[self._start_line:self._end_line+1]
            else:
                df_subset = df.iloc[self._start_line:]

            for _, row in df_subset.iterrows():
                row_id = row["id"]
                prompt_text = row["prompt"]
                
                # --- Retry Logic Starts Here ---
                result = None
                wait_time = 1.0  # Start with 1 second
                max_wait = 64.0  # Maximum wait time between retries
                
                while result is None:
                    try:
                        result = self._model.generate(prompt_text)
                    except Exception as e:
                        # Logic: If it's a rate limit, wait and try again
                        # You can check 'if "rate limit" in str(e).lower():' if needed
                        print(f"Rate limit or error encountered: {e}. Retrying in {wait_time}s...")
                        time.sleep(wait_time)
                        wait_time = min(wait_time * 2, max_wait) 
                # --- Retry Logic Ends Here ---

                self._result_df.loc[row_id] = [row_id, prompt_text, result]
                self._result_df.to_json(
                    f"{self._output_dir}/{language.value}_{speceficity}.jsonl",
                    orient="records",
                    lines=True,
                    force_ascii=False,
                )
                
                # Small polite delay for standard pacing
                time.sleep(0.5)
                yield prompt_text, result


if __name__ == "__main__":
    print("ok")
