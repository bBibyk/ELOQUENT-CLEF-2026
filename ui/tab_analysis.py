# ui/tab_analysis.py
import streamlit as st
import pandas as pd
import json

def render_analysis(current_config):
    """Gère l'affichage des métriques, des graphiques et de l'export."""
    
    if not st.session_state.get('run_done', False):
        st.info("Lancez d'abord une expérimentation dans l'onglet 'Lancement & Suivi' pour voir les résultats.")
        return

    config_to_export = st.session_state.get('last_config', current_config)

    # --- Layout compact avec 2 colonnes principales ---
    col_left, col_right = st.columns([1.5, 1], gap="large")
    
    with col_left:
        # 1. Statistiques (Lot D)
        st.markdown("**Statistiques & Benchmark**")
        sc1, sc2, sc3 = st.columns(3)
        sc1.metric("Longueur moy.", "42 mots", "-5")
        sc2.metric("Vides", "0.5%", "-1.2%", delta_color="inverse")
        sc3.metric("Cohérence", "0.85", "+0.12")
        
    with col_right:
        # 2. Analyse Qualitative (Lot D)
        st.markdown("**Analyse Qualitative**")
        with st.expander("Voir un exemple d'hallucination", expanded=False):
            st.markdown("**FR (unspecific)** : Décris un petit-déjeuner typique.")
            st.error("*Un croissant, une baguette et un café noir.*")
            st.info("💡 Stéréotype détecté[cite: 7].")

    st.markdown("---")

    # 3. Export (Lot E)
    st.markdown("### 📦 Package de Soumission (Challenge)")
    st.caption("Générez les fichiers requis pour clore votre participation.")
    
    st.info("L'exportation de l'archive ZIP complète est encore en cours de développement côté back-end. Merci d'exporter les fichiers indépendamment.")
    
    # MOCK : Données factices pour l'export
    df_mock = pd.DataFrame([{"id": "q1", "prompt": "Test", "answer": "Réponse"}])
    jsonl_data = df_mock.to_json(orient="records", lines=True)
    metadata_json = json.dumps(config_to_export, indent=2)

    st.download_button("📦 Télécharger l'archive complète (.zip)", data=b"", file_name="archive.zip", disabled=True, use_container_width=True, help="Fonctionnalité d'archivage non développée côté backend.")

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.download_button("📄 Télécharger Réponses (.jsonl)", data=jsonl_data, file_name=f"answers_{config_to_export['model']}.jsonl", mime="application/jsonlines", use_container_width=True)
    with col_btn2:
        st.download_button("🛠️ Télécharger Métadonnées (.json)", data=metadata_json, file_name="metadata.json", mime="application/json", use_container_width=True)