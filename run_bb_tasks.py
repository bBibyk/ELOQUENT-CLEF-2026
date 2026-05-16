"""
Script pour exécuter les tâches assignées à Max dans le tableau Excel.
Modèles  : Llama 3.1 (8B) [Groq]  +  Mistral NeMo [Mistral AI]
Langues  : Espagnol uniquement (les fichiers Thai ne sont pas dans le dataset)
Configs  : 
  - Vanilla     : temp=0, do_sample=False, max_tokens=200, pas de prompting
  - Sys. Eng.   : temp=0.7, system_prompt="Eres de nacionalidad española."
Datasets : specific + unspecific
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()

from src.enums import Model, LanguageCode
from src.experiment import Experiment

LANGUAGES = {LanguageCode.TAMIL}
SYS_PROMPT_ESP = "நீங்கள் தமிழ்நாட்டைச் சேர்ந்தவர்."

TASKS = [
    # (dataset_specific, model_enum, temp, do_sample, sys_prompt, title)
    # ── Specifique ESP ──────────────────────────────────────────────────
    # (True,  Model.LLAMA_3_1_8B,   0.7, True, SYS_PROMPT_ESP, "Specific-UKR | Llama3.1-8B | SysEng"),
    (True,  Model.MISTRAL_NEMO,   0.7, True, SYS_PROMPT_ESP, "Specific-TAMIL | MistralNemo | SysEng"),
    # (False, Model.LLAMA_3_1_8B,   0.7, True, SYS_PROMPT_ESP, "Unspecific-UKR | Llama3.1-8B | SysEng"),
    (False, Model.MISTRAL_NEMO,   0.7, True, SYS_PROMPT_ESP, "Unspecific-TAMIL | MistralNemo | SysEng"),
    
    
    # (False, Model.LLAMA_3_1_8B,   0.0, False, "",             "Unspecific-ESP | Llama3.1-8B | Vanilla"),
    # (False, Model.MISTRAL_NEMO,   0.0, False, "",             "Unspecific-ESP | MistralNemo | Vanilla"),
]


def run_task(specific, model, temperature, do_sample, sys_prompt, title):
    print(f"\n{'='*60}")
    print(f"  DÉMARRAGE : {title}")
    print(f"{'='*60}")
    exp = Experiment(
        model_choice=model,
        languages=LANGUAGES,
        specific=specific,
        do_sample=do_sample,
        temprature=temperature,
        system_prompt=sys_prompt,
        prefix="",
        suffix="",
        experiment_title=title,
        max_new_tokens=200,
    )
    count = 0
    for prompt, result in exp.run():
        count += 1
        print(f"  [{count}] Q: {prompt[:80]}...")
        print(f"       R: {result[:100]}...")
    print(f"\n  ✓ Terminé ({count} questions traitées) → {exp._output_dir}")


if __name__ == "__main__":
    total = len(TASKS)
    for i, task in enumerate(TASKS, 1):
        print(f"\n[{i}/{total}] {task[5]}")
        try:
            run_task(*task)
        except Exception as e:
            print(f"  ✗ ERREUR : {e}")

    print(f"\n{'='*60}")
    print("  Toutes les tâches Max sont terminées.")
    print(f"{'='*60}")
