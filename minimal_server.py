from flask import Flask
from webhook import register_routes

app = Flask(__name__)

register_routes(app)

@app.route("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)