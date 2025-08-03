import os
import sys
import requests
import json
from flask import Flask, send_from_directory, jsonify, request, Response
from flask_cors import CORS
from urllib.parse import urlparse, parse_qs

# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app)

TARGET_API_BASE_URL = "https://text.pollinations.ai"

# Cache for models data
models_cache = None
cache_timestamp = 0
CACHE_DURATION = 300  # 5 minutes

@app.route('/models', methods=['GET'])
def get_models():
    global models_cache, cache_timestamp
    import time
    
    current_time = time.time()
    
    # Return cached data if still valid
    if models_cache and (current_time - cache_timestamp) < CACHE_DURATION:
        return Response(models_cache, mimetype='application/json')
    
    try:
        response = requests.get(f"{TARGET_API_BASE_URL}/models", timeout=10)
        response.raise_for_status()
        
        # Cache the response
        models_cache = response.content
        cache_timestamp = current_time
        
        return Response(response.content, mimetype=response.headers.get('Content-Type', 'application/json'))
    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Failed to fetch models",
            "message": str(e),
            "status": "error"
        }), 500

@app.route('/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def relay_all(subpath):
    # Skip static files and root path
    if subpath.startswith('static/') or subpath in ['', 'index.html']:
        return serve(subpath)
    
    # Handle CORS preflight requests
    if request.method == 'OPTIONS':
        response = Response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,PATCH,OPTIONS')
        return response
    
    try:
        target_url = f"{TARGET_API_BASE_URL}/{subpath}"
        
        # Prepare headers (exclude problematic ones)
        headers = {}
        for key, value in request.headers:
            if key.lower() not in ['host', 'content-length', 'content-encoding']:
                headers[key] = value
        
        # Prepare request data
        request_data = None
        if request.method in ['POST', 'PUT', 'PATCH']:
            if request.is_json:
                request_data = json.dumps(request.get_json())
                headers['Content-Type'] = 'application/json'
            else:
                request_data = request.get_data()
        
        # Make request to target API
        if request.method == 'GET':
            response = requests.get(
                target_url, 
                params=request.args, 
                headers=headers,
                timeout=30,
                stream=True
            )
        elif request.method == 'POST':
            response = requests.post(
                target_url, 
                data=request_data,
                headers=headers,
                timeout=30,
                stream=True
            )
        elif request.method == 'PUT':
            response = requests.put(
                target_url, 
                data=request_data,
                headers=headers,
                timeout=30,
                stream=True
            )
        elif request.method == 'DELETE':
            response = requests.delete(
                target_url, 
                headers=headers,
                timeout=30
            )
        elif request.method == 'PATCH':
            response = requests.patch(
                target_url, 
                data=request_data,
                headers=headers,
                timeout=30,
                stream=True
            )
        else:
            return jsonify({"error": "Method not allowed"}), 405

        response.raise_for_status()

        # Prepare response headers
        response_headers = {}
        for key, value in response.headers.items():
            if key.lower() not in ['content-encoding', 'transfer-encoding']:
                response_headers[key] = value
        
        # Add CORS headers
        response_headers['Access-Control-Allow-Origin'] = '*'
        response_headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,PATCH,OPTIONS'
        response_headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'

        # Stream the response back to the client
        def generate():
            try:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        yield chunk
            except Exception as e:
                print(f"Error streaming response: {e}")

        return Response(
            generate(), 
            status=response.status_code,
            headers=response_headers,
            mimetype=response.headers.get('Content-Type', 'application/json')
        )

    except requests.exceptions.Timeout:
        return jsonify({
            "error": "Request timeout",
            "message": "The request took too long to complete",
            "status": "timeout"
        }), 408
    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Connection error",
            "message": "Unable to connect to the target API",
            "status": "connection_error"
        }), 503
    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Request failed",
            "message": str(e),
            "status": "error"
        }), 500

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

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring"""
    try:
        # Test connection to target API
        response = requests.get(f"{TARGET_API_BASE_URL}/models", timeout=5)
        status = "healthy" if response.status_code == 200 else "degraded"
    except:
        status = "unhealthy"
    
    return jsonify({
        "status": status,
        "timestamp": "2025-01-01T00:00:00Z",
        "version": "1.0.0"
    })

@app.route('/api/status', methods=['GET'])
def api_status():
    """Detailed API status endpoint"""
    try:
        response = requests.get(f"{TARGET_API_BASE_URL}/models", timeout=5)
        target_api_status = "online" if response.status_code == 200 else "degraded"
    except:
        target_api_status = "offline"
    
    return jsonify({
        "service": "FullAI Gateway",
        "status": "online",
        "target_api": {
            "url": TARGET_API_BASE_URL,
            "status": target_api_status
        },
        "features": [
            "Text Models (DeepSeek, Grok, GPT)",
            "Multimodal Models (Mistral, GPT-4.1)",
            "Audio Models (GPT-4o Audio)",
            "Special Models (SearchGPT, BIDARA, MIDIjourney)"
        ],
        "supported_methods": ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not found",
        "message": "The requested resource was not found",
        "status": "error"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred",
        "status": "error"
    }), 500

# For Vercel
app_instance = app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

