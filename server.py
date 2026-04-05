from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Store the phone token here
PHONE_TOKEN = None

@app.route("/")
def home():
    return "Phone Control Server Running 🔥"

@app.route("/register_phone", methods=["POST"])
def register_phone():
    global PHONE_TOKEN
    data = request.get_json()
    PHONE_TOKEN = data.get("token")
    return {"status": "Phone Registered", "token": PHONE_TOKEN}

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    cmd = data.get("cmd")

    if not PHONE_TOKEN:
        return {"error": "Phone not connected"}

    requests.post(PHONE_TOKEN, json={"command": cmd})
    return {"status": "Command Sent", "command": cmd}


app.run(host="0.0.0.0", port=5000)
