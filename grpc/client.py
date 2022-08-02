from flask import Flask
from dotenv import load_dotenv
from PIL import Image
from utils.pb_handler import API_Client
from utils.bytes2image import bytes2image
import settings
load_dotenv()

app = Flask("client")

app.config["api"] = API_Client(f"{settings.BACKEND_HOST}:{settings.BACKEND_PORT}")

@app.route("/")
def home():
    api = app.config['api']
    # Code for String Requests
    return api.StringRequest("Hello World!")
    
    # # Code for Image Requests
    # res = api.ImageRequest()
    # [width, height, image_data] = res
    # bytes2image(image_data) # Image downloading
    # return f"Width: {width}, height: {height}"
