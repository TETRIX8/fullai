import requests
from flask import Blueprint, jsonify, request, Response

relay_bp = Blueprint('relay', __name__)

TARGET_API_BASE_URL = "https://text.pollinations.ai"

@relay_bp.route('/models', methods=['GET'])
def get_models():
    try:
        response = requests.get(f"{TARGET_API_BASE_URL}/models")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return Response(response.content, mimetype=response.headers['Content-Type'])
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@relay_bp.route('/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def relay_all(subpath):
    try:
        target_url = f"{TARGET_API_BASE_URL}/{subpath}"
        headers = {key: value for key, value in request.headers if key != 'Host'}
        
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

        return Response(generate(), mimetype=response.headers['Content-Type'])

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


