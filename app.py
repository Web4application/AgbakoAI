from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Configurations
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return "File uploaded successfully", 200
    return render_template('upload.html')

@app.route('/set-domain', methods=['POST'])
def set_domain():
    domain = request.json.get('domain')
    if domain:
        # Simulate domain setting logic
        return jsonify({"message": f"Domain {domain} set successfully"}), 200
    return jsonify({"message": "Invalid domain"}), 400

if __name__ == '__main__':
    app.run(debug=True)
