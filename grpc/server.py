from flask import Flask, request
import os

# Server starter
SERVER_NAME = 'server'
os.system('. venv/bin/activate')
os.system(f'export FLASK_APP={SERVER_NAME}')
os.system('flask run')

# Server description
app = Flask(SERVER_NAME)

# The app is quiet simple, so there are not so much
# sence to make multi-routing server 
@app.route("/")
def greeting():
    return "Welcome to my Flask gRPC app!"
