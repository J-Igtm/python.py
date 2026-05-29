from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is my first Cloud Computing App."

@app.route("/about")
def about():
    return "This app can run on cloud server."

if __name__ == "__main__":
    app.run(debug=True)