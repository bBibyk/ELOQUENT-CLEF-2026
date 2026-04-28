# ui/sidebar.py
import streamlit as st
import sys
import os

# Ajouter src au PYTHONPATH pour importer les enumerations
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.enums import Model, LanguageCode


def render_sidebar():
    """Génère la barre latérale (basée 100% sur src.enums) et retourne la configuration Enum-ready."""

    with st.sidebar:
        st.markdown(
            "<h3 style='margin-top: -40px; margin-bottom: 20px; font-size: 1.1em;'>Configuration du Run</h3>",
            unsafe_allow_html=True,
        )

        def get_default(key, default_val):
            return st.session_state.get(f"config_{key}", default_val)

        # 0. Rejouer une session
        with st.expander("Rejouer une configuration - In development", expanded=False):
            st.info("Cette fonctionnalité n'est pas encore développée côté back-end.")
            st.caption(
                "Elle permettra de restaurer les paramètres exacts d'une ancienne expérience."
            )

            replay_mode = st.radio(
                "Méthode de chargement",
                ["Depuis l'ordinateur (Upload)", "Depuis l'historique local"],
            )

            if replay_mode == "Depuis l'ordinateur (Upload)":
                st.file_uploader(
                    "Fichier de configuration (.json, .jsonl)",
                    type=["json", "jsonl"],
                    disabled=True,
                )
            else:
                st.selectbox(
                    "Expériences enregistrées",
                    [
                        "gemini_2.5_flash_20260313_182005",
                        "mistral_nemo_20260312_091500",
                    ],
                    disabled=True,
                )

            st.button("Charger les paramètres", disabled=True, use_container_width=True)

        # 1. Sélection du Modèle (Directement depuis l'Enum)
        with st.expander("Modèle", expanded=True):
            model_options = list(Model)
            mod_def = get_default("model", model_options[0].name)

            # Retrouve l'index basé sur le nom sauvegardé
            mod_idx = next(
                (i for i, m in enumerate(model_options) if m.name == mod_def), 0
            )

            selected_model = st.selectbox(
                "Modèle", model_options, format_func=lambda m: m.value, index=mod_idx
            )

            # Affichage dynamique des infos du modèle
            try:
                provider = selected_model.to_model_class().__module__.split(".")[-1]
                st.caption(f"Provider: {provider.capitalize().replace('_', ' ')}")
            except Exception:
                pass

        # 2. Données et Langues
        with st.expander("Données et Langues", expanded=True):
            ds_def = get_default("dataset_type", "specific")
            dataset_type = st.radio(
                "Type de Dataset",
                ["unspecific (Diversité)", "specific (Robustesse)"],
                index=1 if "specific" in ds_def else 0,
            )

            all_langs = list(LanguageCode)

            # Initialisation par défaut si vide
            if "config_languages_input" not in st.session_state:
                # Retrouver les valeurs sauvegardées s'il y en a, sinon les 5 par défaut
                default_names = get_default(
                    "languages", ["FRENCH", "ENGLISH", "SPANISH", "GERMAN", "ITALIAN"]
                )
                st.session_state["config_languages_input"] = [
                    l for l in all_langs if l.name in default_names
                ]

            selected_langs = st.multiselect(
                "Langues (5 minimum)",
                options=all_langs,
                format_func=lambda x: f"{x.name.capitalize()} ({x.value})",
                key="config_languages_input",
            )

            if len(selected_langs) < 5:
                st.warning("La baseline exige au moins 5 langues.")

        # 3. Plage de données
        with st.expander("Plage de données (Lignes)", expanded=True):
            dataset_code_str = dataset_type.split(" ")[0]
            # if specific selected 4140 else 101
            max_id = 4140 if dataset_type == "specific (Robustesse)" else 101
            try:
                file_path = f"data/input/en_{dataset_code_str}.jsonl"
                if os.path.exists(file_path):
                    import json

                    with open(file_path, "r", encoding="utf-8") as f:
                        ids = [json.loads(line)["id"] for line in f if line.strip()]
                    max_id = max(int(i) for i in ids)
            except Exception:
                pass

            start_def = get_default("start_line", 0)
            end_def = get_default("end_line", max_id)

            if start_def > max_id:
                start_def = 0
            if end_def > max_id:
                end_def = max_id
            if start_def > end_def:
                start_def = 0

            col1, col2 = st.columns(2)
            with col1:
                start_line = st.number_input(
                    "Début (ID)", min_value=0, max_value=max_id, value=start_def, step=1
                )
            with col2:
                end_line = st.number_input(
                    "Fin (ID)", min_value=0, max_value=max_id, value=end_def, step=1
                )

            if start_line > end_line:
                st.warning("Attention : l'intervalle est invalide (Début > Fin).")

        # 4. Variantes
        with st.expander("Stratégie (Variantes)", expanded=True):
            var_options = ["Vanilla", "Prompt Engineering", "System Engineering"]

            # Initialisation robuste pour le sélecteur
            if "config_variant_state" not in st.session_state:
                var_def = get_default("variant", "Vanilla")
                st.session_state["config_variant_state"] = (
                    var_def if var_def in var_options else "Vanilla"
                )

            variant = st.selectbox(
                "Expérience",
                var_options,
                key="config_variant_state",
                help="""
**Vanilla** : Le modèle répond naturellement sans modification de consigne.
**Prompt Engineering** : Ajoute un préfixe et/ou suffixe à chaque message utilisateur pour forcer un aspect (ex: neutralité).
**System Engineering** : Définit un 'System Prompt' global qui conditionne le comportement général du modèle.
""",
            )

            sys_prompt_input = ""
            prefix_input = ""
            suffix_input = ""

            if variant == "System Engineering":
                sys_prompt_input = st.text_area(
                    "System Prompt",
                    value="Exemple : Tu es un assistant utile spécialisé dans les descriptions objectives et culturellement neutres. Évite les stéréotypes.",
                    height=250,
                    help="Astuce: Si vous êtes sur un petit écran, vous pouvez agrandir verticalement cette zone en tirant le coin inférieur droit.",
                )
            elif variant == "Prompt Engineering":
                prefix_input = st.text_area(
                    "Préfixe (avant la question)",
                    value="Exemple : Veuillez fournir une réponse en vous concentrant sur la diversité culturelle, en évitant les clichés courants : ",
                    height=200,
                    help="Astuce: Tirez sur le coin en bas à droite pour agrandir la zone.",
                )
                suffix_input = st.text_area(
                    "Suffixe (après la question)", value="", height=150
                )

        # 4. Paramètres de Modèle
        with st.expander("Paramètres de Modèle", expanded=False):
            temperature = st.slider(
                "Température",
                0.0,
                2.0,
                get_default("temperature", 0.0),
                0.1,
                help="Gère la créativité. 0 = déterministe, 2 = très créatif.",
            )
            do_sample = st.checkbox(
                "Do Sample",
                value=get_default("do_sample", False),
                help="Active l'échantillonnage stochastique. Si désactivé, le modèle utilise une génération déterministe (greedy).",
            )
            max_new_tokens = st.number_input(
                "Longueur (Max New Tokens)",
                10,
                2048,
                get_default("max_new_tokens", 200),
                step=50,
                help="Le nombre maximum de nouveaux tokens générés dans la réponse.",
            )

        # Retourne des objets typés propres (Enum Model, List[Enum LanguageCode])
        config_dict = {
            "model": selected_model,
            "dataset_type": dataset_type.split(" ")[0],
            "languages": selected_langs,
            "variant": variant,
            "sys_prompt_input": sys_prompt_input,
            "prefix_input": prefix_input,
            "suffix_input": suffix_input,
            "temperature": temperature,
            "do_sample": do_sample,
            "max_new_tokens": max_new_tokens,
            "start_line": start_line,
            "end_line": end_line,
        }

        # Sauvegarde en session (uniquement les str/int pour sérialisation interne)
        for k, v in config_dict.items():
            if k == "model":
                st.session_state[f"config_{k}"] = v.name
            elif k == "languages":
                st.session_state[f"config_{k}"] = [l.name for l in v]
            else:
                st.session_state[f"config_{k}"] = v

        return config_dict
