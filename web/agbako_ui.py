from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_treatment', methods=['POST'])
def get_treatment():
    symptom = request.form.get('symptom', '')
    try:
        response = requests.post(
            'http://localhost:5000/predict_treatment',
            json={"symptom": symptom},
            timeout=5
        )
        response.raise_for_status()
        prediction = response.json()
        return jsonify(prediction)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to get treatment prediction", "details": str(e)}), 500
