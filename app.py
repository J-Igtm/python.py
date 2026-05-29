from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Joginder Next Level Portfolio</title>
    <style>
        body{
            margin:0;
            font-family:Arial, sans-serif;
            background:#020617;
            color:white;
        }
        .hero{
            text-align:center;
            padding:70px 20px;
            background:linear-gradient(135deg,#0f172a,#1e3a8a);
        }
        .profile{
            width:140px;
            height:140px;
            border-radius:50%;
            border:4px solid #38bdf8;
            background:#334155;
            display:inline-flex;
            align-items:center;
            justify-content:center;
            font-size:55px;
            font-weight:bold;
        }
        h1{color:#38bdf8;font-size:46px;}
        .btn{
            display:inline-block;
            margin:10px;
            padding:12px 25px;
            background:#38bdf8;
            color:#020617;
            text-decoration:none;
            border-radius:25px;
            font-weight:bold;
        }
        .section{
            max-width:1050px;
            margin:35px auto;
            padding:30px;
            background:#1e293b;
            border-radius:18px;
            text-align:center;
        }
        .skills span{
            display:inline-block;
            background:#334155;
            margin:8px;
            padding:10px 18px;
            border-radius:20px;
        }
        .bar{
            background:#334155;
            border-radius:20px;
            margin:15px auto;
            max-width:700px;
            overflow:hidden;
        }
        .fill{
            background:#38bdf8;
            padding:10px;
            color:#020617;
            font-weight:bold;
        }
        .projects{
            display:flex;
            gap:20px;
            justify-content:center;
            flex-wrap:wrap;
        }
        .card{
            background:#334155;
            width:260px;
            padding:20px;
            border-radius:15px;
        }
        .card h3{color:#38bdf8;}
        input, textarea{
            width:80%;
            padding:12px;
            margin:8px;
            border-radius:8px;
            border:none;
        }
        button{
            padding:12px 25px;
            background:#38bdf8;
            border:none;
            border-radius:20px;
            font-weight:bold;
        }
        footer{
            text-align:center;
            padding:20px;
            background:#020617;
        }
    </style>
</head>

<body>

<div class="hero">
    <div class="profile">J</div>
    <h1>Joginder Kumar Sharma</h1>
    <h2>Python Developer | Cloud Learner | Cyber Security Beginner</h2>
    <a class="btn" href="https://github.com/J-Igtm" target="_blank">GitHub</a>
    <a class="btn" href="#projects">Projects</a>
    <a class="btn" href="#contact">Contact</a>
</div>

<div class="section">
    <h2>About Me</h2>
    <p>
        I am learning Python, Flask, GitHub, Render Cloud, Blockchain,
        and Cyber Security. This portfolio is deployed live on Render.
    </p>
</div>

<div class="section">
    <h2>Education</h2>
    <p>BCA Student</p>
    <p>Learning Cloud Computing, Cyber Security and Full Stack Development</p>
</div>

<div class="section skills">
    <h2>Skills</h2>
    <span>Python</span>
    <span>Flask</span>
    <span>Git</span>
    <span>GitHub</span>
    <span>HTML</span>
    <span>CSS</span>
    <span>Cloud Computing</span>
    <span>Cyber Security</span>

    <h2>Skill Progress</h2>
    <div class="bar"><div class="fill" style="width:85%">Python 85%</div></div>
    <div class="bar"><div class="fill" style="width:75%">Flask 75%</div></div>
    <div class="bar"><div class="fill" style="width:80%">GitHub 80%</div></div>
    <div class="bar"><div class="fill" style="width:70%">Cloud 70%</div></div>
</div>

<div class="section" id="projects">
    <h2>Projects</h2>
    <div class="projects">
        <div class="card">
            <h3>Cloud Portfolio</h3>
            <p>Portfolio website deployed using Flask and Render.</p>
            <a class="btn" href="#">View</a>
        </div>

        <div class="card">
            <h3>Password Manager</h3>
            <p>Python app to manage passwords securely.</p>
            <a class="btn" href="#">View</a>
        </div>

        <div class="card">
            <h3>Network Scanner</h3>
            <p>Cyber security tool for basic network scanning.</p>
            <a class="btn" href="#">View</a>
        </div>

        <div class="card">
            <h3>Blockchain Certificate</h3>
            <p>DApp idea for certificate verification.</p>
            <a class="btn" href="#">View</a>
        </div>
    </div>
</div>

<div class="section" id="contact">
    <h2>Contact Me</h2>
    <form>
        <input type="text" placeholder="Your Name"><br>
        <input type="email" placeholder="Your Email"><br>
        <textarea rows="5" placeholder="Your Message"></textarea><br>
        <button type="button">Send Message</button>
    </form>
    <p>Email: joginderkumarsharma58@gmail.com</p>
</div>

<footer>
    <p>© 2026 Joginder Kumar Sharma</p>
    <p>Built with Flask + GitHub + Render Cloud</p>
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()