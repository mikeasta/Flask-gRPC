# Protobuf compiler
import os
from dotenv import load_dotenv

load_dotenv()

PATH_TO_PROTOBUF_SRC = os.getenv('PATH_TO_PROTOBUF_SRC')
PATH_TO_PROTOBUF_DST = os.getenv('PATH_TO_PROTOBUF_DST')
PROTOBUF_FILENAME    = os.getenv('PROTOBUF_FILENAME')

# Protocol Buffer Compiler
def pb_compiler(\
    src=PATH_TO_PROTOBUF_SRC,\
    dst=PATH_TO_PROTOBUF_DST,\
    filename=PROTOBUF_FILENAME):
    command = f'protoc -I={src} --python_out={dst} {src}/{filename}.proto'
    os.system(command)

if __name__ == "__main__":
    pb_compiler()