from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

@app.route('/')
def index():
    return jsonify({"message": "AgbakoAI Backend Running"})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file.save(f"uploads/{file.filename}")
    return jsonify({"message": "File uploaded successfully"}), 200

@app.route('/set-domain', methods=['POST'])
def set_domain():
    domain = request.json.get('domain')
    if domain:
        return jsonify({"message": f"Domain {domain} set successfully"}), 200
    return jsonify({"message": "Invalid domain"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
