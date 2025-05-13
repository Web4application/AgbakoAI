from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_treatment', methods=['POST'])
def get_treatment():
    symptom = request.form['symptom']
    response = requests.post('http://localhost:5000/predict_treatment', json={"symptom": symptom})
    prediction = response.json()
    return jsonify(prediction)
