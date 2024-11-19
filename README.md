# Recommandation de Livres - Application Flask

Cette application Flask permet d'afficher des recommandations de livres pour un utilisateur donné. Les recommandations sont obtenues à partir d'une fonction Azure.

---

## Table des matières

1. [Description]
2. [Fonctionnalités]
3. [Technologies Utilisées]
4. [Prérequis]
5. [Installation]
6. [Utilisation]
7. [Tests Unitaires]
8. [Structure du Projet]
9. [Contributions]
10. [Licence]

---

## Description

Cette application permet d'afficher des articles recommandés pour un utilisateur, en fonction de son **ID utilisateur**. L'interface utilisateur est simple et conviviale, avec un formulaire pour entrer l'ID et une table affichant les recommandations.

Les recommandations sont récupérées via une API externe (fonction Azure). En cas d'erreur (ID non valide ou problème réseau), des messages d'erreur explicatifs sont affichés.

---

## Fonctionnalités

- Entrée d'un ID utilisateur via un formulaire.
- Récupération des articles recommandés depuis une API.
- Affichage des recommandations sous forme de table.
- Gestion des erreurs d'entrée utilisateur ou d'API.
- Tests unitaires pour garantir la fiabilité du code.

---

## Technologies Utilisées

- **Langage Backend :** Python (Flask)
- **Frontend :** HTML, CSS
- **API externe :** Azure Functions
- **Tests :** Unittest, Mock
- **Dépendances :** 
  - `requests`
  - `Flask`

---

## Prérequis

- **Python 3.9+** doit être installé.
- Un environnement virtuel Python configuré.
- Une connexion réseau pour interroger l'API externe.

---

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo

2. Créez un environnement virtuel :

    python -m venv venv
    source venv/bin/activate  # Sur Linux/MacOS
    venv\Scripts\activate     # Sur Windows

3. Installez les dépendances :

    pip install -r requirements.txt
   
4. Configurez l'URL de l'API Azure dans le fichier app.py :

    AZURE_FUNCTION_URL = 'https://votre-fonction-azure-url/api/reco_api'

5. Lancez l'application :

    python app.py

6. Ouvrez votre navigateur à l'adresse :

    http://127.0.0.1:5000

## Utilisation
Entrez un ID utilisateur dans le formulaire de la page principale.
Cliquez sur "Voir les recommandations".
Si l'API renvoie des articles, ceux-ci s'afficheront dans une table.
Si aucune recommandation n'est trouvée ou si une erreur survient, un message s'affiche.

## Tests Unitaires
Des tests unitaires garantissent le bon fonctionnement de l'application. Pour exécuter les tests, utilisez :

bash
Copier le code
python -m unittest test_app.py

## Structure du Projet

├── app.py                 # Fichier principal de l'application Flask

├── templates/
│   
    └── index.html         # Interface utilisateur

├── static/                # (Si applicable) CSS, JS, Images

├── test_app.py            # Tests unitaires

├── requirements.txt       # Liste des dépendances Python

└── README.md              # Ce fichier



## Contributions
Les contributions sont les bienvenues ! 
Pour contribuer :

Forkez le dépôt.
Créez une branche pour vos modifications :
bash
Copier le code
git checkout -b feature/ma-nouvelle-fonctionnalite
Faites vos modifications, ajoutez des tests si nécessaire.
Soumettez une pull request.

## Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.

markdown
Copier le code

### Instructions pour l’utiliser :

- Remplacez `votre-utilisateur/votre-repo` et `votre-fonction-azure-url` par les valeurs réelles.
- Ajoutez les informations spécifiques à votre projet si nécessaire.
