# Protobuf compiler
import os
from dotenv import load_dotenv

load_dotenv()

PATH_TO_PROTOBUF_SRC = os.getenv('PATH_TO_PROTOBUF_SRC')
PATH_TO_PROTOBUF_DST = os.getenv('PATH_TO_PROTOBUF_DST')
PROTOBUF_FILENAMES   = os.getenv('PROTOBUF_FILENAMES')

# Protocol Buffer Compiler
def pb_compiler(\
    src=PATH_TO_PROTOBUF_SRC,\
    dst=PATH_TO_PROTOBUF_DST,\
    filenames=PROTOBUF_FILENAMES):

    # Make sure that file names in .env files
    # are written in the next format
    # name_one_without_'.proto',name_two_without_'.proto',...
    filenames = filenames.split(',')

    # Compiling every chosen .proto file
    for filename in filenames:
        command = f'python -m grpc_tools.protoc -I={src} --python_out={dst} --grpc_python_out={dst} {src}/{filename}.proto'
        os.system(command)

if __name__ == "__main__":
    pb_compiler()