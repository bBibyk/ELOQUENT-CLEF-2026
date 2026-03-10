# ui/sidebar.py
import streamlit as st

def render_sidebar():
    """Génère la barre latérale et retourne le dictionnaire de configuration."""
    
    LANGUAGES_DICT = {
        "fr": "Français", "en": "Anglais", "es": "Espagnol",
        "de": "Allemand", "it": "Italien", "ar": "Arabe", "zh": "Chinois"
    }

    with st.sidebar:
        st.markdown("<h3 style='margin-top: -40px; margin-bottom: 20px; font-size: 1.1em;'>Configuration du Run</h3>", unsafe_allow_html=True)
        
        # 1. Sélection du Modèle / Provider [cite: 33]
        with st.expander("Modèle", expanded=True):
            provider = st.selectbox("Provider", ["OpenAI (API)", "Ollama (Local)"])
            model_name = st.selectbox("Modèle", ["gpt-4o-mini", "gpt-3.5-turbo"] if provider == "OpenAI (API)" else ["llama3", "mistral"])
            
        # 2. Données et Langues [cite: 33]
        with st.expander("Données et Langues", expanded=True):
            dataset_type = st.radio("Dataset", ["unspecific (Diversité)", "specific (Robustesse)"])
            
            # Astuce UI : Bouton pour tout sélectionner
            if st.button("Toutes les langues"):
                st.session_state.selected_langs = list(LANGUAGES_DICT.keys())
                
            selected_langs = st.multiselect(
                "Langues", 
                options=list(LANGUAGES_DICT.keys()),
                format_func=lambda x: LANGUAGES_DICT[x],
                default=st.session_state.get('selected_langs', ["fr", "en", "es", "de", "it"])
            )
            st.session_state.selected_langs = selected_langs
            
            if len(selected_langs) < 5:
                st.warning("La baseline exige au moins 5 langues[cite: 30].")
        
        # 3. Variantes (Lot C)
        with st.expander("Stratégie (Variantes)", expanded=True):
            variant = st.selectbox("Expérience", ["Baseline (Vanilla)", "System Prompt", "Reformulation auto"])
        
        # 4. Hyperparamètres 
        with st.expander("Paramètres", expanded=False):
            temperature = st.slider("Température", 0.0, 2.0, 0.0, 0.1)
            max_tokens = st.number_input("Max Tokens", 10, 500, 50)

        # Retourne la configuration complète pour assurer la reproductibilité 
        return {
            "provider": provider,
            "model": model_name,
            "dataset_type": dataset_type.split(" ")[0],
            "languages": selected_langs,
            "variant": variant,
            "temperature": temperature,
            "max_tokens": max_tokens
        }