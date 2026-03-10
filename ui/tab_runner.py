# ui/tab_runner.py
import streamlit as st
import sys
import os

# Ajouter le dossier parent au path pour importer src.experiment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    from src.experiment import Experiment
except ImportError:
    pass

def render_runner(config):
    """Gère l'affichage du lancement et du suivi de l'exécution."""
    
    # config['model'] est désormais une instance d'Enum Model : on utilise .value pour l'affichage
    st.markdown(f"**Prêt à lancer** : `{config['model'].value}` • `{config['dataset_type']}` • `{len(config['languages'])} langues` • `{config['variant']}`")
    
    if st.button("Lancer l'expérimentation", use_container_width=True, type="primary"):
        if not config['languages']:
            st.error("Veuillez sélectionner au moins une langue.")
            return
            
        st.info("Initialisation de l'expérience via src/experiment.py...")
        
        try:
            # On passe directement les enums du dictionnaire config ! Plus de conversion avec des "if gemini in ..."
            exp = Experiment(
                model_choice=config['model'],
                languages=set(config['languages']),
                do_sample=(config['temperature'] > 0),
                temprature=config['temperature'],
                title=f"Exp: {config['variant']}"
            )
            
            progress_bar = st.progress(0)
            log_box = st.empty()
            logs = "Démarrage du run...\n"
            
            # Boucle sur le générateur de résultats intermédiaires
            for i, res in enumerate(exp.run()):
                logs += f"{res}\n"
                log_box.text_area("Console de Logs", logs, height=150)
                # Mise à jour arbitraire de la barre pour cet exemple mocké
                progress_val = min((i + 1) / 10, 1.0)
                progress_bar.progress(progress_val)
                
            progress_bar.progress(1.0)
            st.success("Exécution terminée ! Les résultats sont dans l'onglet Analyse & Export.")
            
            st.session_state['run_done'] = True
            
            # Pour l'export JSON dans tab_analysis, on transforme nos Énums en strings simples
            export_config = config.copy()
            export_config['model'] = config['model'].value
            export_config['languages'] = [l.value for l in config['languages']]
            st.session_state['last_config'] = export_config
            
        except Exception as e:
            st.error(f"Erreur lors de l'exécution de l'expérience : {e}")