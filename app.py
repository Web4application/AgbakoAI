from flask import Flask, request, jsonify, render_template
import os
import logging

# --- Initialize Flask app ---
app = Flask(__name__)

# --- Configurations ---
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Setup logging for visibility
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Helper function ---
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            logging.warning("No file part in request")
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            logging.warning("No file selected")
            return "No selected file", 400
        if file and allowed_file(file.filename):
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(save_path)
            logging.info(f"File saved to {save_path}")
            return "File uploaded successfully", 200
        else:
            logging.warning("File extension not allowed")
            return "Invalid file type", 400
    return render_template('upload.html')

@app.route('/set-domain', methods=['POST'])
def set_domain():
    domain = request.json.get('domain')
    if domain:
        # Implement your domain-setting logic here
        logging.info(f"Domain set to: {domain}")
        return jsonify({"message": f"Domain {domain} set successfully"}), 200
    else:
        logging.warning("No domain provided")
        return jsonify({"message": "Invalid domain"}), 400

@app.route('/ai/analyze', methods=['POST'])
def ai_analyze():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Dummy AgbakoAI analysis simulation (replace with your real AI module)
    from agbakoAI import AgbakoAI  # Make sure agbakoAI.py is in the same directory or installed as a package
    ai = AgbakoAI()
    result = ai.run_task("analyze", "machine_learning", text)

    return jsonify({"input": text, "analysis": result})

# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True)
