import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__, template_folder='templates')
CORS(app)

# Use your API Key here
try:
    client = genai.Client(api_key="AIzaSyAuaxQUr6Pe-knHQ14syMT3XS7FsZTMTdI")
    print("--- AI Client Initialized ---")
except Exception as e:
    print(f"--- Initialization Error: {e} ---")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    print("--- Received a request! ---")
    data = request.json
    user_message = data.get("message")
    print(f"User Message: {user_message}")
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=user_message
        )
        print(f"AI Response: {response.text}")
        return jsonify({"reply": response.text})
    except Exception as e:
        print(f"GOOGLE API ERROR: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)