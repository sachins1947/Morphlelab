from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {ist_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
