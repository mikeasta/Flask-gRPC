import os
from dotenv import load_dotenv

load_dotenv()

PATH_TO_PROTOBUF_SRC = os.getenv('PATH_TO_PROTOBUF_SRC')
PATH_TO_PROTOBUF_DST = os.getenv('PATH_TO_PROTOBUF_DST')
PROTOBUF_FILENAME    = os.getenv('PROTOBUF_FILENAME')