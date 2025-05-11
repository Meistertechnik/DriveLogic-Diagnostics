from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "DriveLogic Diagnostics is online!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are DriveLogic, a highly skilled automotive diagnostic assistant. You specialize in diagnosing vehicle issues based on trouble codes, symptoms, and vehicle models. Always be clear, concise, and informative."},
            {"role": "user", "content": user_input}
        ]
    )
    return jsonify({"reply": response.choices[0].message["content"]})