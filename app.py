from flask import Flask, request, jsonify, render_template
import requests
import time

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get", methods=["GET"])

def get_response():
    user_message = request.args.get("msg")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    for _ in range(2):  # Try twice
        response = requests.post(
            RASA_URL,
            json={"sender": "user", "message": user_message},
            timeout=10
        )
        if response.status_code == 200 and response.json():
            rasa_response = response.json()
            bot_message = rasa_response[0].get("text", "Sorry, I didn't understand that.")
            return jsonify({"response": bot_message})
        time.sleep(1)  # Wait a second before retrying
    
    return jsonify({"response": "No response from Rasa"}), 500


if __name__ == "__main__":
    app.run(port=5000)
