import os
import io
import grpc 
import sys
import numpy as np
from dotenv import load_dotenv
from PIL import Image
from numproto import ndarray_to_proto, proto_to_ndarray
from messages.msg_pb2 import StringMessage, NDArrayMessage, ImageMessage, Response
from messages.msg_pb2_grpc import FlaskServiceServicer, FlaskServiceStub

# Enable messages import
sys.path.append('../')

# Request server handler
class API_Server(FlaskServiceServicer):
    def StringRequest(self, request, context):
        return StringMessage(msg=request.msg)

    def NDArrayRequest(self, request, context):
        return NDArrayMessage(ndarray=request.ndarray)
    
    def ImageRequest(self, request, context):
        return ImageMessage(width=request.width, height=request.height, image_data=request.image_data)

# Request client handler
class API_Client:
    def __init__(self, target):
        channel = grpc.insecure_channel(target)
        self.client = FlaskServiceStub(channel)
    
    def StringRequest(self, message):
        protobuf = StringMessage(msg=message)
        response = self.client.StringRequest(protobuf)
        return response.msg
    
    def NDArrayRequest(self, array):
        ndarray = ndarray_to_proto(np.array(array))
        protobuf = NDArrayMessage(ndarray=ndarray)
        response = self.client.NDArrayRequest(protobuf)
        return proto_to_ndarray(response.ndarray)

    def ImageRequest(self):
        load_dotenv()
        INPUT_IMAGE_NAME = os.getenv("INPUT_IMAGE_NAME")
        image = Image.open(INPUT_IMAGE_NAME)
        width, height = image.size[0], image.size[1]
        imageByteArr = io.BytesIO()
        image.save(imageByteArr, format=image.format)
        image_data = imageByteArr.getvalue()
        protobuf = ImageMessage(width=width, height=height, image_data=image_data)
        response = self.client.ImageRequest(protobuf)
        return [response.width, response.height, response.image_data]