from flask import Flask
import webhook

app = Flask(__name__)

# Register webhook routes
webhook.register_routes(app)

@app.route("/ping")
def ping():
    return "pong"