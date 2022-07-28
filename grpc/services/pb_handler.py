import grpc 
import numpy as np
from numproto import ndarray_to_proto, proto_to_ndarray
from messages.msg_pb2 import StringMessage, NDArrayMessage, ImageMessage, Response
from messages.msg_pb2_grpc import FlaskServiceServicer, FlaskServiceStub

# Request server handler
class API_Server(FlaskServiceServicer):
    def SendStringMessage(self, request, context):
        return StringMessage(msg=request.msg)

    def SendNDArrayMessage(self, request, context):
        return NDArrayMessage(ndarray=request.ndarray)

# Request client handler
class API_Client:
    def __init__(self, target):
        channel = grpc.insecure_channel(target)
        self.client = FlaskServiceStub(channel)

    def SendStringMessage(self, string):
        response = self.client.SendStringMessage(StringMessage(msg=string))
        return response.msg

    def SendNDArrayMessage(self, array):
        array = np.array(array)
        response = self.client.SendNDArrayMessage(NDArrayMessage(ndarray=ndarray_to_proto(array)))
        return proto_to_ndarray(response.ndarray)
