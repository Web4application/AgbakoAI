from core.disease_knowledge import DiseaseKnowledge
from flask import Flask, jsonify, request

app = Flask(__name__)
disease_knowledge = DiseaseKnowledge()

@app.route('/disease/<name>', methods=['GET'])
def get_disease(name):
    disease = disease_knowledge.get_disease_details(name)
    if disease:
        return jsonify({"name": disease[0], "description": disease[1], "symptoms": disease[2], "cure_found": disease[3]})
    else:
        return jsonify({"error": "Disease not found"}), 404
