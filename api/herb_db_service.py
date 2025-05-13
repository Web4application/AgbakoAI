from core.herb_knowledge import HerbKnowledge
from flask import Flask, jsonify, request

app = Flask(__name__)
herb_knowledge = HerbKnowledge()

@app.route('/herb/<name>', methods=['GET'])
def get_herb(name):
    herb = herb_knowledge.get_herb_details(name)
    if herb:
        return jsonify({"name": herb[0], "description": herb[1], "usage": herb[2], "chemical_properties": herb[3]})
    else:
        return jsonify({"error": "Herb not found"}), 404
