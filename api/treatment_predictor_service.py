from core.treatment_predictor import TreatmentPredictor
from flask import Flask, jsonify, request

app = Flask(__name__)
treatment_predictor = TreatmentPredictor()

@app.route('/predict_treatment', methods=['POST'])
def predict_treatment():
    symptom = request.json.get('symptom')
    if not symptom:
        return jsonify({"error": "Symptom is required"}), 400
    
    prediction = treatment_predictor.predict_treatment(symptom)
    return jsonify({"prediction": prediction})
