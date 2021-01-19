from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<p>Welcome to Flask</p>'

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1')