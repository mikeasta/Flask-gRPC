# @mikeasta - 02/08/2022
# Release 
# Description: Syncronous gRPC micro-service that performs
# using Flask and Protobuf for delivery simple data structures 

# This file automatically:
# - installs all dependencies
# - compiles all .proto files in the choosed directory

# Server and client start manually

import os
import sys
from grpc.utils.pb_compiler import pb_compiler

sys.path.append('grpc/utils')
os.system("pip install -r requirements.txt")

pb_compiler()