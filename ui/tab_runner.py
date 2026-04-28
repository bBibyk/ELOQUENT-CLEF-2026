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
            # --- Construction des prompts selon la Variante ---
            sys_prompt = config.get("sys_prompt_input", "")
            prefix_str = config.get("prefix_input", "")
            suffix_str = config.get("suffix_input", "")
                
            # Instanciation de l'expérience avec les bons paramètres de prompt
            exp = Experiment(
                model_choice=config['model'],
                languages=set(config['languages']),
                do_sample=config['do_sample'],
                temprature=config['temperature'],
                system_prompt=sys_prompt,
                prefix=prefix_str,
                suffix=suffix_str,
                experiment_title=f"Exp: {config['variant']}",
                specific=config['dataset_type'] == 'specific',
                start_line=config['start_line'],
                end_line=config['end_line'],
                max_new_tokens=config['max_new_tokens']
            )
            
            total_tasks = (config['end_line'] - config['start_line'] + 1) * len(config['languages'])
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            log_box = st.empty()
            log_box.info("Démarrage du run...")
            
            
            # Boucle sur le générateur de résultats intermédiaires
            for i, (prompt, res) in enumerate(exp.run()):
                with log_box.container():
                    st.markdown("**Requête actuelle :**")
                    st.info(prompt)
                    st.markdown("**Réponse du modèle :**")
                    st.success(res)
                
                # Mise à jour arbitraire de la barre pour cet exemple mocké
                progress_val = min((i + 1) / max(1, total_tasks), 1.0)
                progress_bar.progress(progress_val)
                remaining = total_tasks - (i + 1)
                status_text.markdown(f"**Progression** : {i+1} / {total_tasks} lignes traitées | **Restantes** : {remaining}")
                
            progress_bar.progress(1.0)
            st.success("Exécution terminée ! Les résultats ont été sauvegardés.")
            
            st.session_state['run_done'] = True
            
            # Pour l'export JSON dans tab_analysis, on transforme nos Énums en strings simples
            export_config = config.copy()
            export_config['model'] = config['model'].value
            export_config['languages'] = [l.value for l in config['languages']]
            st.session_state['last_config'] = export_config
            
        except Exception as e:
            st.error(f"Erreur lors de l'exécution de l'expérience : {e}")