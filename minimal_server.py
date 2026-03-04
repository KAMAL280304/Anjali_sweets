from flask import Flask

app = Flask(__name__)

# Import routes AFTER creating app
import webhook

@app.route("/ping")
def ping():
    return "pong"