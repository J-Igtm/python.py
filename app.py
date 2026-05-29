from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Joginder Portfolio</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: white;
        }
        .hero {
            text-align: center;
            padding: 80px 20px;
            background: linear-gradient(135deg, #1e293b, #0f172a);
        }
        .hero h1 {
            font-size: 48px;
            color: #38bdf8;
        }
        .hero p {
            font-size: 22px;
        }
        .btn {
            display: inline-block;
            margin: 10px;
            padding: 12px 25px;
            background: #38bdf8;
            color: #0f172a;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
        }
        .section {
            max-width: 1000px;
            margin: 40px auto;
            padding: 30px;
            background: #1e293b;
            border-radius: 15px;
            text-align: center;
        }
        .skills span {
            display: inline-block;
            background: #334155;
            padding: 10px 18px;
            margin: 8px;
            border-radius: 20px;
        }
        .projects {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        .card {
            background: #334155;
            padding: 20px;
            border-radius: 12px;
            width: 260px;
        }
        .card h3 {
            color: #38bdf8;
        }
        .contact p {
            font-size: 18px;
        }
        footer {
            text-align: center;
            padding: 20px;
            background: #020617;
        }
    </style>
</head>

<body>

    <div class="hero">
        <h1>Joginder Kumar Sharma</h1>
        <p>Python Developer | Cloud Computing Learner | Cyber Security Beginner</p>
        <a class="btn" href="https://github.com/J-Igtm" target="_blank">GitHub</a>
        <a class="btn" href="#contact">Contact Me</a>
        <a class="btn" href="#">Download Resume</a>
    </div>

    <div class="section">
        <h2>About Me</h2>
        <p>
            I am learning Python, Flask, GitHub, Render Cloud, Blockchain,
            and Cyber Security. This is my professional portfolio website
            deployed on Render Cloud.
        </p>
    </div>

    <div class="section skills">
        <h2>Skills</h2>
        <span>Python</span>
        <span>Flask</span>
        <span>Git</span>
        <span>GitHub</span>
        <span>Cloud Computing</span>
        <span>Cyber Security</span>
        <span>Blockchain</span>
        <span>HTML</span>
        <span>CSS</span>
    </div>

    <div class="section">
        <h2>Projects</h2>
        <div class="projects">
            <div class="card">
                <h3>Cloud Portfolio</h3>
                <p>Portfolio website deployed using Flask and Render.</p>
            </div>

            <div class="card">
                <h3>Password Manager</h3>
                <p>Python project to store and manage passwords securely.</p>
            </div>

            <div class="card">
                <h3>Network Scanner</h3>
                <p>Cyber security tool for scanning devices on a network.</p>
            </div>

            <div class="card">
                <h3>Blockchain Certificate</h3>
                <p>DApp for certificate verification using blockchain.</p>
            </div>
        </div>
    </div>

    <div class="section contact" id="contact">
        <h2>Contact</h2>
        <p>Email: joginderkumarsharma58@gmail.com</p>
        <p>GitHub: J-Igtm</p>
    </div>

    <footer>
        <p>© 2026 Joginder Kumar Sharma | Built with Flask and Render</p>
    </footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()