from flask import Flask
import webhook

app = Flask(__name__)
@app.route("/webhook-test")
def webhook_test():
    return "webhook route works"
# Import routes AFTER creating app


@app.route("/ping")
def ping():
    return "pong"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)