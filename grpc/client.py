# Client program
from flask import Flask
from utils.pb_handler import API_Client
from utils.bytes2image import bytes2image
import settings

app = Flask("client")

app.config["api"] = API_Client(f"{settings.BACKEND_HOST}:{settings.BACKEND_PORT}")

@app.route("/")
def home():
    api = app.config['api']

    # Uncomment special code block
    # for transfering actual data type
    
    # Code for String Requests
    return api.StringRequest("Hello World!")
    
    # # Code for NDArray requests
    # return api.NDArrayRequest([[1, 2, 3], [4, 5, 6]])

    # # Code for Image Requests
    # res = api.ImageRequest()
    # [width, height, image_data] = res
    # bytes2image(image_data) # Image downloading
    # return f"Width: {width}, height: {height}"