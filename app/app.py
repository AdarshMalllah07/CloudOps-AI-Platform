from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>CloudOps AI Platform</h1>
    <p>Application running successfully.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)