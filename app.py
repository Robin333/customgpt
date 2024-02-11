from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Ensure that the path to the JSON file is correct relative to your Flask app's root
JSON_DATA_PATH = os.path.join(app.root_path, 'tfidf_data.json')

@app.route('/api/vector-data', methods=['GET'])
def get_vector_data():
    try:
        # Serve the JSON file directly
        return send_from_directory(directory=app.root_path, path='tfidf_data.json')
    except FileNotFoundError:
        return jsonify({"error": "Vector data file not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Adjust the port if necessary
