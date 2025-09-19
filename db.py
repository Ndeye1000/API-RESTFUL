import sqlite3

# Connexion (crée le fichier si inexistant)
conn = sqlite3.connect("ma_base.db")
cursor = conn.cursor()

# Création de la table
cursor.execute("""
CREATE TABLE IF NOT EXISTS fruits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    quantite INTEGER NOT NULL,
    prix_unite REAL NOT NULL
)
""")

# Exemple d’insertion
cursor.execute("INSERT INTO fruits (nom, quantite, prix_unite) VALUES (?, ?, ?)", ("fraise 🍓", 10, 250))

conn.commit()
conn.close()