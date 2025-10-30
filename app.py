# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from the DevOps Project! The current time is: 8:36 '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
