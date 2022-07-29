from flask import Flask, render_template

import settings
from services.pb_handler import API_Client

app = Flask(__name__)

app.config["api"] = API_Client(f"{settings.BACKEND_HOST}:{settings.BACKEND_PORT}")

@app.route("/")
def home():
    return 'Hello world'
