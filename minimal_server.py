from flask import Flask

app = Flask(__name__)

# Import routes AFTER creating app
import webhook

@app.route("/ping")
def ping():
    return "pong"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)