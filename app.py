from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Joginder Portfolio</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background:#0f172a;
                color:white;
                text-align:center;
                margin:0;
            }

            .header{
                padding:50px;
                background:#1e293b;
            }

            .section{
                margin:30px;
                padding:20px;
                background:#334155;
                border-radius:10px;
            }

            h1{
                color:#38bdf8;
            }

            ul{
                list-style:none;
                padding:0;
            }

            li{
                padding:5px;
            }

            .btn{
                display:inline-block;
                padding:12px 25px;
                background:#38bdf8;
                color:white;
                text-decoration:none;
                border-radius:25px;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <h1>Joginder Kumar Sharma</h1>
            <h3>Python Developer | Cloud Computing Learner</h3>
        </div>

        <div class="section">
            <h2>About Me</h2>
            <p>
            I am learning Python, Flask, GitHub, Render Cloud,
            Blockchain and Cyber Security.
            </p>
        </div>

        <div class="section">
            <h2>Skills</h2>
            <ul>
                <li>Python</li>
                <li>Flask</li>
                <li>Git & GitHub</li>
                <li>Cloud Computing</li>
                <li>Cyber Security</li>
                <li>Blockchain</li>
            </ul>
        </div>

        <div class="section">
            <h2>Projects</h2>
            <ul>
                <li>Cloud Portfolio Website</li>
                <li>Password Manager</li>
                <li>Network Scanner</li>
                <li>Blockchain Certificate Verification</li>
            </ul>
        </div>

        <div class="section">
            <h2>Contact</h2>
            <p>Email: joginderkumarsharma58@gmail.com</p>
        </div>

        <br>
        <a class="btn" href="/">Home</a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()