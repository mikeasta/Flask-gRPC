from urllib import response
import grpc 
import numpy as np
from numproto import ndarray_to_proto, proto_to_ndarray
from msg_pb2 import StringMessage, NDArrayMessage, ImageMessage, Response
from msg_pb2_grpc import FlaskServiceServicer, FlaskServiceStub

# Request server handler
class API_Server(FlaskServiceServicer):
    def StringRequest(self, request, context):
        return StringMessage(msg=request.msg)

# Request client handler
class API_Client:
    def __init__(self, target):
        channel = grpc.insecure_channel(target)
        self.client = FlaskServiceStub(channel)
    
    def StringRequest(self, message):
        protobuf = StringMessage(msg=message)
        response = self.client.StringRequest(protobuf)
        return response.msg

