# ui/sidebar.py
import streamlit as st
import sys
import os

# Ajouter src au PYTHONPATH pour importer les enumerations
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.enums import Model, LanguageCode

def render_sidebar():
    """Génère la barre latérale (basée 100% sur src.enums) et retourne la configuration Enum-ready."""
    
    with st.sidebar:
        st.markdown("<h3 style='margin-top: -40px; margin-bottom: 20px; font-size: 1.1em;'>Configuration du Run</h3>", unsafe_allow_html=True)

        def get_default(key, default_val):
            return st.session_state.get(f"config_{key}", default_val)
        
        # 1. Sélection du Modèle (Directement depuis l'Enum)
        with st.expander("Modèle", expanded=True):
            model_options = list(Model)
            mod_def = get_default("model", model_options[0].name)
            
            # Retrouve l'index basé sur le nom sauvegardé
            mod_idx = next((i for i, m in enumerate(model_options) if m.name == mod_def), 0)
            
            selected_model = st.selectbox(
                "Modèle", 
                model_options, 
                format_func=lambda m: m.value, 
                index=mod_idx
            )
            
            # Affichage dynamique des infos du modèle
            if selected_model == Model.GEMINI_2_0_FLASH:
                st.caption("via Google AI Studio (Free Tier)")
            elif selected_model == Model.MISTRAL_NEMO:
                st.caption("Modèle On-premise (12B)")
            
        # 2. Données et Langues
        with st.expander("Données et Langues", expanded=True):
            ds_def = get_default("dataset_type", "unspecific")
            dataset_type = st.radio("Dataset", ["unspecific (Diversité)", "specific (Robustesse)"], index=0 if "unspecific" in ds_def else 1)
            
            all_langs = list(LanguageCode)
            if st.button("Toutes les langues"):
                st.session_state["config_languages"] = [l.name for l in all_langs]
                
            # Les 5 langues par défaut pour démarrer (en Enums)
            default_langs = [LanguageCode.FRENCH, LanguageCode.ENGLISH, LanguageCode.SPANISH, LanguageCode.GERMAN, LanguageCode.ITALIAN]
            saved_lang_names = get_default("languages", [l.name for l in default_langs])
            
            # Reconstruction de la liste d'Enums sélectionnée par défaut
            default_selection = [l for l in all_langs if l.name in saved_lang_names]
            
            selected_langs = st.multiselect(
                "Langues", 
                options=all_langs,
                format_func=lambda x: f"{x.name.capitalize().replace('_', ' ')} ({x.value})",
                default=default_selection
            )
            
            if len(selected_langs) < 5:
                st.warning("La baseline exige au moins 5 langues.")
        
        # 3. Variantes 
        with st.expander("Stratégie (Variantes)", expanded=True):
            var_def = get_default("variant", "Baseline (Vanilla)")
            var_options = ["Baseline (Vanilla)", "System Prompt", "Reformulation auto"]
            var_idx = var_options.index(var_def) if var_def in var_options else 0
            variant = st.selectbox("Expérience", var_options, index=var_idx)
        
        # 4. Hyperparamètres
        with st.expander("Paramètres", expanded=False):
            temperature = st.slider("Température", 0.0, 2.0, get_default("temperature", 0.0), 0.1)
            top_p = st.slider("Top-p", 0.0, 1.0, get_default("top_p", 1.0), 0.05)
            max_tokens = st.number_input("Max Tokens", 10, 2048, get_default("max_tokens", 500), step=50)
            seed_val = get_default("seed", 42)
            seed = st.number_input("Déterminisme (Seed)", 0, 100000, seed_val if seed_val is not None else 42)

        # Retourne des objets typés propres (Enum Model, List[Enum LanguageCode])
        config_dict = {
            "model": selected_model,
            "dataset_type": dataset_type.split(" ")[0],
            "languages": selected_langs,
            "variant": variant,
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens,
            "seed": seed
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