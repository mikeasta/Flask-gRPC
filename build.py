# 1. Compile Protobuf's
import os
from config import PATH_TO_PROTOBUF_SRC, PATH_TO_PROTOBUF_DST, PROTOBUF_FILENAME

command = f'protoc -I={PATH_TO_PROTOBUF_SRC} --python_out={PATH_TO_PROTOBUF_DST} {PATH_TO_PROTOBUF_SRC}/{PROTOBUF_FILENAME}.proto'
os.system(command)

# 2. Run server 