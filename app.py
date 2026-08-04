from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from PaaS Lab! Student: shakthiya narayanan R, Roll No: 24MIC0036'
