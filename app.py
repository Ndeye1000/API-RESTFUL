from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de donnees simulée
liste_utilisateurs = [
    {"id": 1, "nom": "Kine"},
    {"id": 2, "nom": "Khadim"},
    {"id": 3, "nom": "Astou"}
]

@app.route('/api/utilisateurs', methods=['GET'])
def obtenir_utilisateurs():
    return jsonify(liste_utilisateurs)

@app.route('/api/utilisateurs/<int:id>', methods=['GET'])
def obtenir_utilisateur(id):    
    utilisateur = next((u for u in liste_utilisateurs if u["id"] == id), None)
    if utilisateur:
        return jsonify(utilisateur)
    else:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    
@app.route('/api/utilisateurs', methods=['POST'])
def ajouter_utilisateur():
    nouveau_utilisateur = request.get_json()
    liste_utilisateurs.append(nouveau_utilisateur)
    return jsonify(nouveau_utilisateur), 201

@app.route('/api/utilisateurs/<int:id>', methods=['PUT'])
def mettre_a_jour_utilisateur(id):
    utilisateur = next((u for u in liste_utilisateurs if u["id"] == id), None)
    if utilisateur:
        donnees = request.get_json()
        utilisateur.update(donnees)
        return jsonify(utilisateur)
    else:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    
@app.route('/api/utilisateurs/<int:id>', methods=['DELETE'])
def supprimer_utilisateur(id):
    global liste_utilisateurs
    liste_utilisateurs = [u for u in liste_utilisateurs if u["id"] != id]
    return jsonify({"message": "Utilisateur supprimé"}), 200

if __name__ == '__main__':
    app.run(debug=True)