from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

def get_fruits():
    conn = sqlite3.connect("ma_base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nom, quantite, prix_unite FROM fruits")
    fruits = cursor.fetchall()
    conn.close()
    return fruits

@app.route("/")
def index():
    fruits = get_fruits()
    return render_template("index.html", fruits=fruits)


@app.route('/api/fruits', methods=['GET'])
def obtenir_fruits():
    return jsonify(liste_fruits)

@app.route('/api/fruits/<int:id>', methods=['GET'])
def obtenir_utilisateur(id):    
    utilisateur = next((u for u in liste_fruits if u["id"] == id), None)
    if utilisateur:
        return jsonify(utilisateur)
    else:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    
@app.route('/api/fruits', methods=['POST'])
def ajouter_utilisateur():
    nouveau_utilisateur = request.get_json()
    liste_fruits.append(nouveau_utilisateur)
    return jsonify(nouveau_utilisateur), 201

@app.route('/api/fruits/<int:id>', methods=['PUT'])
def mettre_a_jour_utilisateur(id):
    utilisateur = next((u for u in liste_fruits if u["id"] == id), None)
    if utilisateur:
        donnees = request.get_json()
        utilisateur.update(donnees)
        return jsonify(utilisateur)
    else:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    
@app.route('/api/fruits/<int:id>', methods=['DELETE'])
def supprimer_utilisateur(id):
    global liste_fruits
    liste_fruits = [u for u in liste_fruits if u["id"] != id]
    return jsonify({"message": "Utilisateur supprimé"}), 200

if __name__ == '__main__':
    app.run(debug=True)