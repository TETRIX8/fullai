import os
import sys
import requests
from flask import Flask, send_from_directory, jsonify, request, Response
from flask_cors import CORS

# DON\'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app)

TARGET_API_BASE_URL = "https://text.pollinations.ai"

@app.route('/models', methods=['GET'])
def get_models():
    try:
        response = requests.get(f"{TARGET_API_BASE_URL}/models")
        response.raise_for_status()
        return Response(response.content, mimetype=response.headers.get('Content-Type', 'application/json'))
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def relay_all(subpath):
    # Skip static files and root path
    if subpath.startswith('static/') or subpath in ['', 'index.html']:
        return serve(subpath)
    
    try:
        target_url = f"{TARGET_API_BASE_URL}/{subpath}"
        headers = {key: value for key, value in request.headers if key.lower() not in ['host', 'content-length']}
        
        if request.method == 'GET':
            response = requests.get(target_url, params=request.args, headers=headers)
        elif request.method == 'POST':
            response = requests.post(target_url, data=request.get_data(), headers=headers, stream=True)
        elif request.method == 'PUT':
            response = requests.put(target_url, data=request.get_data(), headers=headers, stream=True)
        elif request.method == 'DELETE':
            response = requests.delete(target_url, headers=headers)
        else:
            return jsonify({"error": "Method not allowed"}), 405

        response.raise_for_status()

        # Stream the response back to the client
        def generate():
            for chunk in response.iter_content(chunk_size=8192):
                yield chunk

        return Response(generate(), mimetype=response.headers.get('Content-Type', 'application/json'))

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', defaults={'path': ''})
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

# For Vercel
app_instance = app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

