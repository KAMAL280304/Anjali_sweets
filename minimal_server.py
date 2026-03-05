from flask import Flask
from webhook import register_routes
import os

app = Flask(__name__)

register_routes(app)

@app.route("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)