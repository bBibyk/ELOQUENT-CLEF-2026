# ELOQUENT @ CLEF 2026

Application multi-LLM realisee dans le cadre du projet MIAGE M2 Big Data Analytics autour du challenge ELOQUENT "Cultural Robustness & Diversity".

L'application permet de :

- lancer des experimentations sur les jeux de donnees JSONL du challenge ;
- comparer plusieurs familles de modeles ;
- tester plusieurs strategies de prompting ;
- generer des sorties JSONL et des metadonnees de run.

Le point d'entree principal du projet est l'interface Streamlit : `app.py`.

## Demarrage rapide

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

Une fois le serveur lance, ouvrez `http://localhost:8501` dans votre navigateur.

## Installation from scratch

### 1. Prerequis

- Python installe sur la machine
- Une connexion Internet pour appeler les API des modeles
- Au moins une cle d'API active selon le provider choisi

Python 3.10+ est recommande.

### 2. Recuperer le projet

Si le depot n'est pas encore present :

```bash
git clone <url-du-depot>
cd ELOQUENT-CLEF-2026
```

Si le depot est deja ouvert dans votre IDE, placez-vous simplement dans le dossier `ELOQUENT-CLEF-2026`.

### 3. Creer un environnement virtuel

L'environnement virtuel est fortement recommande pour isoler les dependances du projet.

Windows PowerShell :

```powershell
python -m venv .venv
```

macOS / Linux :

```bash
python3 -m venv .venv
```

### 4. Installer les dependances

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

## Configuration des cles API

Le projet utilise actuellement des providers distants. Il faut donc renseigner une ou plusieurs cles d'API dans un fichier `.env`.

1. Dupliquez le fichier d'exemple :

Windows PowerShell :

```powershell
Copy-Item .env.example .env
```

macOS / Linux :

```bash
cp .env.example .env
```

2. Ouvrez `.env` et renseignez uniquement les variables utiles pour les modeles que vous souhaitez utiliser.

Variables reconnues par le code :

- `GOOGLE_API_KEY` pour les modeles Gemini / Gemma exposes via Google
- `MISTRAL_API_KEY` pour les modeles Mistral
- `GROQ_API_KEY` pour les modeles servis via Groq
- `DEEPSEEK_API_KEY` pour `DeepSeek Chat`

Exemple minimal :

```env
GOOGLE_API_KEY=your_google_key_here
MISTRAL_API_KEY=
GROQ_API_KEY=
DEEPSEEK_API_KEY=
```

Important :

- il suffit d'avoir la cle correspondant au modele selectionne dans l'interface ;
- sans cle valide, le lancement de l'interface fonctionne, mais l'execution du run echouera au moment d'interroger le provider ;
- dans cette version du depot, les providers implementes sont API-first. Un provider local open-source via endpoint local n'est pas encore branche dans ce code.

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

1. choisissez un modele ;
2. choisissez le type de dataset : `specific` ou `unspecific` ;
3. selectionnez les langues ;
4. laissez `Vanilla`, ou activez une variante de prompt ;
5. lancez l'experimentation.

Les jeux de donnees d'entree sont deja presents dans `data/input/`.

Les sorties sont ecrites automatiquement dans `data/output/<model>_<timestamp>/` avec :

- un ou plusieurs fichiers JSONL contenant les reponses generees ;
- un fichier `submission_metadata.json` qui capture les parametres du run.

## Reproduire une baseline conforme au sujet

Pour une baseline simple conforme aux attentes du projet :

- selectionnez `Vanilla` ;
- gardez une temperature a `0.0` pour un comportement deterministe ;
- ne renseignez ni `System Prompt`, ni prefixe, ni suffixe ;
- selectionnez au moins 5 langues ;
- choisissez la plage de lignes a traiter ;
- lancez le run.

Cette configuration correspond a l'idee d'un run sans reformulation ni prompt engineering, avec une session independante par question.

## Structure utile du depot

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

Note : le dossier `configs/` existe deja, mais l'execution actuelle passe principalement par l'interface Streamlit et les metadonnees sauvegardees dans `data/output/`.

## Depannage rapide

- `ModuleNotFoundError` : relancez l'installation avec `pip install -r requirements.txt`.
- Erreur de provider ou quota : verifiez la cle d'API correspondant au modele choisi.
- Rien n'apparait dans `data/output/` : le dossier n'est cree qu'au moment du lancement effectif d'un run.
- L'onglet export reste partiellement mocke : l'interface d'analyse/export est encore en cours de finalisation cote backend.

## Document complementaire

Un document de travail dedie aux variantes susceptibles d'introduire des biais culturels est disponible ici :

- [IDEES_VARIANTES_BIAIS_CULTURELS.md](./IDEES_VARIANTES_BIAIS_CULTURELS.md)
