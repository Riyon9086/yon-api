from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Tentukan direktori untuk menyimpan video yang di-upload
UPLOAD_FOLDER = 'videos'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return jsonify({'name': 'RyonXD'})

# Rute untuk mengunggah video
@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video part'}), 400

    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No selected video'}), 400

    if file:
        # Simpan video ke folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return jsonify({'message': 'Video uploaded successfully!', 'filename': file.filename}), 201

# Rute untuk mengakses video yang telah di-upload
@app.route('/videos/<filename>', methods=['GET'])
def get_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
