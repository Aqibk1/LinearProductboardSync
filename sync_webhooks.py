import os
import json
import hmac
import hashlib
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

PRODUCTBOARD_API_KEY = os.getenv("PRODUCTBOARD_API_KEY")
LINEAR_API_KEY = os.getenv("LINEAR_API_KEY")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

def verify_signature(payload, signature):
    if not WEBHOOK_SECRET:
        return False
    expected_signature = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_signature, signature)

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Hub-Signature-256")
    if not signature or not verify_signature(request.data, signature):
        return jsonify({"error": "Invalid signature"}), 403
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400
    
    event_type = request.headers.get("X-GitHub-Event")
    if event_type == "productboard_update":
        update_linear_status(data)
    elif event_type == "linear_update":
        update_productboard_status(data)
    else:
        return jsonify({"error": "Unknown event type"}), 400
    
    return jsonify({"status": "success"})

def update_linear_status(data):
    linear_id = data.get("linear_id")
    status = data.get("status")
    
    if not linear_id or not status:
        return
    
    headers = {"Authorization": f"Bearer {LINEAR_API_KEY}", "Content-Type": "application/json"}
    payload = {"query": f"mutation {{ updateIssue(id: \"{linear_id}\", input: {{ state: \"{status}\" }}) {{ issue {{ id }} }} }}"}
    response = requests.post("https://api.linear.app/graphql", headers=headers, json=payload)
    response.raise_for_status()

def update_productboard_status(data):
    productboard_id = data.get("productboard_id")
    status = data.get("status")
    
    if not productboard_id or not status:
        return
    
    headers = {"Authorization": f"Bearer {PRODUCTBOARD_API_KEY}", "Content-Type": "application/json"}
    payload = {"data": {"status": status}}
    response = requests.put(f"https://api.productboard.com/items/{productboard_id}", headers=headers, json=payload)
    response.raise_for_status()

if __name__ == "__main__":
    app.run(port=5000)
