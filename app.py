from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Joginder Cloud App</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                text-align: center;
            }
            .container {
                padding-top: 120px;
            }
            h1 {
                font-size: 50px;
                margin-bottom: 10px;
            }
            p {
                font-size: 20px;
                margin-bottom: 30px;
            }
            .btn {
                background: #00c6ff;
                color: white;
                padding: 14px 30px;
                text-decoration: none;
                border-radius: 30px;
                font-size: 18px;
                display: inline-block;
            }
            .btn:hover {
                background: #0072ff;
            }
            .card {
                background: rgba(255,255,255,0.15);
                margin: 40px auto;
                padding: 25px;
                width: 70%;
                border-radius: 15px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome Joginder!</h1>
            <p>My First Professional Cloud Website using Flask and Render.</p>
            <a class="btn" href="/about">About Project</a>

            <div class="card">
                <h2>Cloud Computing Project</h2>
                <p>This app is deployed on Render Cloud and connected with GitHub.</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return """
    <html>
    <head>
        <title>About Project</title>
    </head>
    <body style="font-family:Arial; text-align:center; padding-top:80px;">
        <h1>About This Project</h1>
        <p>This is my first cloud computing project.</p>
        <p>Technology used: Python, Flask, GitHub, Render.</p>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()