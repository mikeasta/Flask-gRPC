# Bytes to image converter
import os
import io
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
OUTPUT_IMAGE_NAME = os.getenv("OUTPUT_IMAGE_NAME")
OUTPUT_IMAGE_PATH = os.getenv("OUTPUT_IMAGE_PATH")

# Converts bytes array to image and
# save it at the special path
def bytes2image(bytes, image_name=OUTPUT_IMAGE_NAME, save_path=OUTPUT_IMAGE_PATH):
    image = Image.open(io.BytesIO(bytes))
    image.save(f'{save_path}/{image_name}')