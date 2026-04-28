Voici ton texte avec les accents correctement ajoutés :

---

# ÉLOQUENT @ CLEF 2026

Application multi-LLM réalisée dans le cadre du projet MIAGE M2 Big Data Analytics autour du challenge ÉLOQUENT "Cultural Robustness & Diversity".

L'application permet de :

* lancer des expérimentations sur les jeux de données JSONL du challenge ;
* comparer plusieurs familles de modèles ;
* tester plusieurs stratégies de prompting ;
* générer des sorties JSONL et des métadonnées de run.

Le point d'entrée principal du projet est l'interface Streamlit : `app.py`.

## Démarrage rapide

### Windows PowerShell

```powershell
cd ELOQUENT-CLEF-2026
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
.\.venv\Scripts\python.exe -m streamlit run app.py
```

### macOS / Linux

```bash
cd ELOQUENT-CLEF-2026
python3 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
./.venv/bin/python -m streamlit run app.py
```

Une fois le serveur lancé, ouvrez `http://localhost:8501` dans votre navigateur.

## Installation from scratch

### 1. Prérequis

* Python installé sur la machine
* Une connexion Internet pour appeler les API des modèles
* Au moins une clé d'API active selon le provider choisi

Python 3.10+ est recommandé.

### 2. Récupérer le projet

Si le dépôt n'est pas encore présent :

```bash
git clone <url-du-depot>
cd ELOQUENT-CLEF-2026
```

Si le dépôt est déjà ouvert dans votre IDE, placez-vous simplement dans le dossier `ELOQUENT-CLEF-2026`.

### 3. Créer un environnement virtuel

L'environnement virtuel est fortement recommandé pour isoler les dépendances du projet.

Windows PowerShell :

```powershell
python -m venv .venv
```

macOS / Linux :

```bash
python3 -m venv .venv
```

### 4. Installer les dépendances

Windows PowerShell :

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

macOS / Linux :

```bash
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
```

## Configuration des clés API

Le projet utilise actuellement des providers distants. Il faut donc renseigner une ou plusieurs clés d'API dans un fichier `.env`.

1. Dupliquez le fichier d'exemple :

Windows PowerShell :

```powershell
Copy-Item .env.example .env
```

macOS / Linux :

```bash
cp .env.example .env
```

2. Ouvrez `.env` et renseignez uniquement les variables utiles pour les modèles que vous souhaitez utiliser.

Variables reconnues par le code :

* `GOOGLE_API_KEY` pour les modèles Gemini / Gemma exposés via Google
* `MISTRAL_API_KEY` pour les modèles Mistral
* `GROQ_API_KEY` pour les modèles servis via Groq
* `DEEPSEEK_API_KEY` pour `DeepSeek Chat`

Exemple minimal :

```env
GOOGLE_API_KEY=your_google_key_here
MISTRAL_API_KEY=
GROQ_API_KEY=
DEEPSEEK_API_KEY=
```

Important :

* il suffit d'avoir la clé correspondant au modèle sélectionné dans l'interface ;
* sans clé valide, le lancement de l'interface fonctionne, mais l'exécution du run échouera au moment d'interroger le provider ;
* dans cette version du dépôt, les providers implémentés sont API-first. Un provider local open-source via endpoint local n'est pas encore branché dans ce code.

## Lancer l'application

Depuis le dossier `ELOQUENT-CLEF-2026` :

Windows PowerShell :

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

macOS / Linux :

```bash
./.venv/bin/python -m streamlit run app.py
```

Si la commande `streamlit run app.py` n'est pas reconnue, gardez la forme `python -m streamlit run app.py`, plus robuste.

## Utilisation minimale

Dans l'interface :

1. choisissez un modèle ;
2. choisissez le type de dataset : `specific` ou `unspecific` ;
3. sélectionnez les langues ;
4. laissez `Vanilla`, ou activez une variante de prompt ;
5. lancez l'expérimentation.

Les jeux de données d'entrée sont déjà présents dans `data/input/`.

Les sorties sont écrites automatiquement dans `data/output/<model>_<timestamp>/` avec :

* un ou plusieurs fichiers JSONL contenant les réponses générées ;
* un fichier `submission_metadata.json` qui capture les paramètres du run.

## Reproduire une baseline conforme au sujet

Pour une baseline simple conforme aux attentes du projet :

* sélectionnez `Vanilla` ;
* gardez une température à `0.0` pour un comportement déterministe ;
* ne renseignez ni `System Prompt`, ni préfixe, ni suffixe ;
* sélectionnez au moins 5 langues ;
* choisissez la plage de lignes à traiter ;
* lancez le run.

Cette configuration correspond à l'idée d'un run sans reformulation ni prompt engineering, avec une session indépendante par question.

## Structure utile du dépôt

```text
ELOQUENT-CLEF-2026/
|- app.py
|- data/input/
|- data/output/
|- src/experiment.py
|- src/models/
|- ui/
|- configs/
`- IDEES_VARIANTES_BIAIS_CULTURELS.md
```

Note : le dossier `configs/` existe déjà, mais l'exécution actuelle passe principalement par l'interface Streamlit et les métadonnées sauvegardées dans `data/output/`.

## Dépannage rapide

* `ModuleNotFoundError` : relancez l'installation avec `pip install -r requirements.txt`.
* Erreur de provider ou quota : vérifiez la clé d'API correspondant au modèle choisi.
* Rien n'apparaît dans `data/output/` : le dossier n'est créé qu'au moment du lancement effectif d'un run.
* L'onglet export reste partiellement mocké : l'interface d'analyse/export est encore en cours de finalisation côté backend.
