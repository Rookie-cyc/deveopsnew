# app.py
from flask import Flask
app = Flask(__name__)
#HELLLLLLLLLO
@app.route('/')
def hello_world():
    return 'Hello from the DevOps Project! The current time is: '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')