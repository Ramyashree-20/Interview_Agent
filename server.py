# server.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, requests, logging
from dotenv import load_dotenv

# Load local .env for development (safe to keep; .env must NOT be committed)
load_dotenv()

# Config
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_GROQ_MODEL = "llama-3.1-8b-instant"

# App
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app, resources={r"/api/*": {"origins": "*"}})  # restrict origins in production

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/api/ask", methods=["POST"])
def ask():
    # Check API key at request time and return useful error if missing
    if not GROQ_API_KEY:
        logger.error("GROQ_API_KEY is not configured")
        return jsonify({"error": "Server misconfiguration: GROQ_API_KEY not set"}), 500

    payload = request.get_json(force=True, silent=True) or {}
    messages = payload.get("messages")
    model = payload.get("model", DEFAULT_GROQ_MODEL)
    temperature = payload.get("temperature", 0.7)

    if not messages:
        return jsonify({"error": "messages field required"}), 400

    groq_payload = {"model": model, "messages": messages, "temperature": temperature}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {GROQ_API_KEY}"}

    try:
        resp = requests.post(GROQ_API_URL, json=groq_payload, headers=headers, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.exception("Groq request failed")
        return jsonify({"error": "Groq request failed", "details": str(e)}), 502

    try:
        return jsonify(resp.json()), 200
    except ValueError:
        return jsonify({"error": "Invalid JSON from Groq", "raw": resp.text}), 502

# Serve static files (index.html + assets) from repo root
@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def static_file(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    # For local development only. In Render use gunicorn via Procfile.
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

