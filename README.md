# API RESTful Fruits

Ce projet est une application Flask qui propose une API RESTful pour gérer une liste de fruits stockée dans une base de données SQLite. Il inclut également une interface web pour afficher les fruits.

## Structure du projet

- `app.py` : Application principale Flask (API et interface web)
- `db.py` : Script d'initialisation de la base de données SQLite
- `ma_base.db` : Base de données SQLite
- `templates/index.html` : Template HTML pour l'affichage des fruits
- `.gitignore` : Fichiers et dossiers ignorés par Git

## Installation

1. **Cloner le dépôt :**
   ```sh
   git clone <url-du-repo>
   cd API-RESTFUL
   ```

2. **Créer un environnement virtuel :**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances :**
   ```sh
   pip install flask
   ```

4. **Initialiser la base de données :**
   ```sh
   python db.py
   ```

## Utilisation

1. **Lancer l'application :**
   ```sh
   python app.py
   ```

2. **Accéder à l'interface web :**
   - Ouvrir [http://127.0.0.1:5000](http://127.0.0.1:5000) dans votre navigateur.

3. **Endpoints API :**

   - `GET /api/fruits` : Liste des fruits
   - `GET /api/fruits/<id>` : Détails d'un fruit par son ID
   - `POST /api/fruits` : Ajouter un fruit
   - `PUT /api/fruits/<id>` : Modifier un fruit
   - `DELETE /api/fruits/<id>` : Supprimer un fruit

## Remarques

- Les données affichées sur la page web proviennent de la base SQLite.
- L'API utilise actuellement une liste en mémoire (`liste_fruits`). Pour une gestion complète via la base de données, adaptez les routes pour interagir avec SQLite.

## Auteur

- Ndeye S. Mergane