from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Cybersecurity Training Program</title>
    </head>
    <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Welcome to the Cybersecurity Training Program</h1>
        <p>All materials provided in this Cybersecurity Training Program, whether online or physical, are the intellectual property of <strong>AfricaHackOn</strong> and <strong>Cyber Guard Africa</strong>.</p>
        <p>Unauthorized sharing, reproduction, or distribution is strictly prohibited and may result in legal action.</p>
        <p>By participating, you agree to use the materials solely for this program and comply with copyright laws.</p>
        <p>For inquiries, contact <a href="mailto:academy@africahackon.com">academy@africahackon.com</a></p>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
