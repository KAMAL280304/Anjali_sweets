from flask import Flask, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong"

@app.route("/webhook", methods=["GET","POST"])
def webhook():

    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == "my_verify_token_123":
            return challenge, 200
        else:
            return "Forbidden", 403

    if request.method == "POST":
        data = request.get_json()
        print("Incoming webhook:", data)
        return "EVENT_RECEIVED", 200