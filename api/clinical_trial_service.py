from models.trial_simulator import TrialSimulator
from flask import Flask, jsonify, request

app = Flask(__name__)
trial_simulator = TrialSimulator()

@app.route('/simulate_trial', methods=['POST'])
def simulate_trial():
    treatment = request.json.get('treatment')
    if not treatment:
        return jsonify({"error": "Treatment is required"}), 400
    
    outcome = trial_simulator.simulate_trial(treatment)
    return jsonify({"outcome": outcome})
