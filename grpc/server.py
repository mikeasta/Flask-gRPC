from flask import Flask
import os

# Server starter
SERVER_FILENAME = 'server'
os.system('. venv/bin/activate')
os.system(f'export FLASK_APP={SERVER_FILENAME}')
os.system('flask run')

# Server description
app = Flask('server')

@app.route("/")
def hello_world():
    return "Hello World!"