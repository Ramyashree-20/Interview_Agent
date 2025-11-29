from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_GROQ_MODEL = "llama-3.1-8b-instant"

app = Flask(__name__, static_folder='.', static_url_path='')  
CORS(app, resources={r"/api/*": {"origins": "*"}})

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in .env")

@app.route("/api/ask", methods=["POST"])
def ask():
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
        return jsonify({"error": "Groq request failed", "details": str(e)}), 502

    return jsonify(resp.json()), 200

@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def static_file(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
