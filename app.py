from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

