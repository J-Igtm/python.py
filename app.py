from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Contact Form</title>
        <style>
            body{
                font-family:Arial;
                background:#0f172a;
                color:white;
                text-align:center;
                padding:50px;
            }
            form{
                background:#1e293b;
                padding:30px;
                border-radius:15px;
                max-width:500px;
                margin:auto;
            }
            input, textarea{
                width:90%;
                padding:12px;
                margin:10px;
                border-radius:8px;
                border:none;
            }
            button{
                background:#38bdf8;
                padding:12px 25px;
                border:none;
                border-radius:20px;
                font-weight:bold;
            }
        </style>
    </head>
    <body>

    <h1>Contact Me</h1>

    <form action="/submit" method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>

        <input type="email" name="email" placeholder="Your Email" required><br>

        <textarea name="message" rows="5"
        placeholder="Your Message" required></textarea><br>

        <button type="submit">Send Message</button>
    </form>

    </body>
    </html>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return f"""
    <html>
    <body style="font-family:Arial;text-align:center;padding:50px;">
        <h1>Thank You {name}!</h1>
        <h3>Your message has been received.</h3>

        <p><b>Email:</b> {email}</p>
        <p><b>Message:</b> {message}</p>

        <a href="/">Back to Home</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()