# ui/tab_runner.py
import streamlit as st
import time

def render_runner(config):
    """Gère l'affichage du lancement et du suivi de l'exécution."""
    
    # Affichage ultra-compact des paramètres
    st.markdown(f"**Prêt à lancer** : `{config['model']}` • `{config['dataset_type']}` • `{len(config['languages'])} langues` • `{config['variant']}`")
    
    if st.button("Lancer l'expérimentation", use_container_width=True, type="primary"):
        if not config['languages']:
            st.error("Veuillez sélectionner au moins une langue.")
            return
            
        st.info("Initialisation du pipeline backend (Lot A)...")
        
        # --- MOCK : Simulation du backend en attendant le vrai code ---
        progress_bar = st.progress(0)
        status_text = st.empty()
        log_box = st.empty()
        logs = "Démarrage du run...\n"
        
        total = 15
        for i in range(total):
            time.sleep(0.1) # Simule l'appel API
            progress_bar.progress((i + 1) / total)
            status_text.text(f"Traitement en cours... Prompt {i+1}/{total}")
            
            # Simulation d'erreur silencieuse demandée par le sujet [cite: 25]
            if i == 5:
                logs += f"[Alerte] Timeout sur le prompt {i}, on continue.\n"
                
            log_box.text_area("Console de Logs", logs, height=150)
            
        st.success("Exécution terminée ! Les résultats sont dans l'onglet Analyse & Export.")
        st.session_state['run_done'] = True
        st.session_state['last_config'] = config