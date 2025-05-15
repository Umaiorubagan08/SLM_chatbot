from flask import Flask, render_template, request, session
from app.chatbot import generate_response



app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        user_input = request.form["message"]
        session["history"].append(f"User: {user_input}")
        bot_reply = generate_response(user_input, session["history"])
        session["history"].append(f"Bot: {bot_reply}")
        return {"reply": bot_reply}

    return render_template("index.html", history=session["history"])

chat_history = []

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = generate_response(user_input, chat_history)
    chat_history.append(user_input)
    chat_history.append(response)
    print("Bot:", response)


if __name__ == "__main__":
    app.run(debug=True)
