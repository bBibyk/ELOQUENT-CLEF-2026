# app.py
import streamlit as st
from ui.sidebar import render_sidebar
from ui.tab_runner import render_runner
from ui.style import apply_clean_theme

# --- CONFIGURATION GLOBALE DE LA PAGE ---
st.set_page_config(page_title="ELOQUENT - Run Manager", layout="wide", initial_sidebar_state="auto")

# 0. Appliquer le thème épuré
apply_clean_theme()

st.markdown("### Projet ELOQUENT : Cultural Robustness & Diversity")
st.markdown("<p style='color: #6B7280; font-size: 0.9em; margin-top: -10px; margin-bottom: 20px;'>Application multi-LLM pour évaluer la robustesse culturelle.</p>", unsafe_allow_html=True)

# 1. Rendu de la barre latérale qui nous retourne la configuration
run_config = render_sidebar()

# 2. Rendu de l'interface principale
render_runner(run_config)