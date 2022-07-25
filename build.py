# 1. Compile Protobuf's
import os
from config import \
    PATH_TO_PROTOBUF_SRC,\
    PATH_TO_PROTOBUF_DST, \
    PROTOBUF_FILENAME

command = f'protoc -I={PATH_TO_PROTOBUF_SRC} --python_out={PATH_TO_PROTOBUF_DST} {PATH_TO_PROTOBUF_SRC}/{PROTOBUF_FILENAME}.proto'
os.system(command)

# 2. Run server 
SERVER_FILENAME = 'server'
os.system('. venv/bin/activate')
os.system(f'export FLASK_APP={SERVER_FILENAME}')
os.system('flask run')