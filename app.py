from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Cloud App</h1>
    <p>This app is running on Render Cloud.</p>
    <a href='/about'>About</a>
    """

@app.route("/about")
def about():
    return """
    <h2>About Me</h2>
    <p>My first cloud computing project deployed with Flask and Render.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)