import os
from flask import Flask
from dotenv import load_dotenv
from PIL import Image
import settings
from utils.pb_handler import API_Client
from utils.bytes2image import bytes2image

load_dotenv()
app = Flask("client")

app.config["api"] = API_Client(f"{settings.BACKEND_HOST}:{settings.BACKEND_PORT}")

@app.route("/")
def home():
    api = app.config['api']
    res = api.ImageRequest()
    [width, height, image_data] = res
    # image = Image.frombytes("RGBA", (width, height), image_data)
    # image.save(os.getenv("OUTPUT_IMAGE_NAME"))
    bytes2image(image_data)
    return f"Width: {width}, height: {height}"
