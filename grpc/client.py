from flask import Flask

import settings
from pb_handler import API_Client

app = Flask("client")

app.config["api"] = API_Client(f"{settings.BACKEND_HOST}:{settings.BACKEND_PORT}")

@app.route("/")
def home():
    api = app.config['api']
    return api.StringRequest('Message sent')
