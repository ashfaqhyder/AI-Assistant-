from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Configure Google Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Use a correct model name (use `list_models.py` to check available models)
MODEL_NAME = "gemini-1.5-pro"  # Update if needed

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        user_prompt = data.get("prompt")
        function_type = data.get("function")  # Get selected function

        if not user_prompt or not function_type:
            return jsonify({"error": "Missing input or function type"}), 400

        # ✅ Modify prompt based on selected function
        if function_type == "question":
            final_prompt = f"Answer this question: {user_prompt}"
        elif function_type == "summarize":
            final_prompt = f"Summarize the following text: {user_prompt}"
        elif function_type == "creative":
            final_prompt = f"Write a creative story or poem about: {user_prompt}"
        else:
            return jsonify({"error": "Invalid function type"}), 400

        # ✅ Generate response using Google Gemini
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(final_prompt)

        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

