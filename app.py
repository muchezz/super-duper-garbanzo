from flask import Flask, request
import socket
import os
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    client_ip = request.remote_addr
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <html>
        <head>
            <title>Cloud Native App</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f0f8ff;
                    padding: 20px;
                }}
                .box {{
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <div class="box">
                <h1>Hello from Cloud Native App! 🌥️</h1>
                <p><strong>Hostname:</strong> {hostname}</p>
                <p><strong>Your IP:</strong> {client_ip}</p>
                <p><strong>Time:</strong> {current_time}</p>
                <p><strong>Environment:</strong></p>
                <ul>
                    <li>ENV: {os.getenv("ENV", "Not Set")}</li>
                    <li>VERSION: {os.getenv("VERSION", "1.0.0")}</li>
                </ul>
            </div>
        </body>
    </html>
    """
    return html

# 👇 Security issue for Bandit to catch
eval("print('This is unsafe')")


# 👇 Security issue for gitleaks-secret-scan to catch
API_KEY = "sk_live_51HV2tpHKZSwXkNth41HAKa2HF922o2eSSwUZYPm"
GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
