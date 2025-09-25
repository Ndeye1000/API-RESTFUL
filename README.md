# API RESTful Fruits

Une API RESTful développée avec Flask pour gérer une base de données de fruits, avec interface web intégrée.

## Technologies utilisées

- Python 3.13
- Flask 
- SQLite3
- HTML/CSS

## Structure du projet

```
API-RESTFUL/
│
├── app.py           # Application principale Flask
├── db.py           # Initialisation de la base de données
├── ma_base.db      # Base de données SQLite
├── templates/      # Templates HTML
│   └── index.html  # Page d'accueil
├── static/         # Fichiers statiques (CSS, JS)
└── .gitignore     # Configuration Git
```

## Prérequis

- Python 3.13 installé
- pip (gestionnaire de paquets Python)

## Installation

1. **Cloner le projet :**
   ```sh
   git clone https://github.com/NdeyeS/API-RESTFUL.git
   cd API-RESTFUL
   ```

2. **Créer l'environnement virtuel :**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

3. **Installer les dépendances :**
   ```sh
   pip install -r requirements.txt
   ```

4. **Initialiser la base de données :**
   ```sh
   python db.py
   ```

## Démarrage

1. **Lancer le serveur :**
   ```sh
   python app.py
   ```

2. **Accéder à l'application :**
   - Interface web : [http://localhost:5000](http://localhost:5000)
   - API : [http://localhost:5000/api/fruits](http://localhost:5000/api/fruits)

## Documentation API

### Endpoints disponibles

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/fruits` | Récupérer tous les fruits |
| GET | `/api/fruits/<id>` | Récupérer un fruit par ID |
| POST | `/api/fruits` | Ajouter un nouveau fruit |
| PUT | `/api/fruits/<id>` | Modifier un fruit existant |
| DELETE | `/api/fruits/<id>` | Supprimer un fruit |

### Exemple de requête POST

```json
{
    "nom": "Pomme",
    "description": "Fruit rouge ou vert",
    "prix": 1.50,
    "quantite": 100
}
```

## Tests

Pour exécuter les tests :
```sh
python -m pytest
```

## Contribution

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Auteur

- **Ndeye S. Mergane** 

