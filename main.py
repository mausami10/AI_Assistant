import os
 
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import OpenAI
 
load_dotenv()
 
app = app = Flask(__name__, static_folder="public", static_url_path="")
 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-6-astra")
 
 
def ask_model(system_prompt, user_prompt):
    response = client.responses.create(
        model=MODEL,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=1.0,
        max_output_tokens=512,
    )
    return response.output_text.strip()
 
 
@app.route("/")
def home():
    return render_template("index.html")
 
 
@app.route("/ask", methods=["POST"])
def ask():
    question = (request.form.get("question") or "").strip()
    if not question:
        return jsonify({"response": "Please enter a question."}), 400
 
    try:
        answer = ask_model("Act like a helpful personal assistant", question)
        return jsonify({"response": answer}), 200
    except Exception as e:
        app.logger.error("Ask error: %s", e)
        return jsonify({"response": "Sorry, something went wrong. Please try again."}), 500
 
 
@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = (request.form.get("email") or "").strip()
    if not email_text:
        return jsonify({"response": "Please enter the email text."}), 400
 
    prompt = f"Summarize the following email in 2-3 sentences: {email_text}"
 
    try:
        summary = ask_model("Act like an expert email assistant", prompt)
        return jsonify({"response": summary}), 200
    except Exception as e:
        app.logger.error("Summarize error: %s", e)
        return jsonify({"response": "Sorry, something went wrong. Please try again."}), 500
 
 
if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1", port=int(os.getenv("PORT", 5000)))