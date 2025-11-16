# relay.py
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # خزنه في إعدادات Render
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")       # خزنه في إعدادات Render

@app.route("/send", methods=["POST"])
def send_to_telegram():
    data = request.json
    message = data.get("message", "No message provided")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}

    try:
        response = requests.post(url, json=payload)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "Relay is running."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
