# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import msg_pb2 as msg__pb2


class FlaskServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StringRequest = channel.unary_unary(
                '/flask_grpc.FlaskService/StringRequest',
                request_serializer=msg__pb2.StringMessage.SerializeToString,
                response_deserializer=msg__pb2.StringMessage.FromString,
                )
        self.NDArrayRequest = channel.unary_unary(
                '/flask_grpc.FlaskService/NDArrayRequest',
                request_serializer=msg__pb2.NDArrayMessage.SerializeToString,
                response_deserializer=msg__pb2.NDArrayMessage.FromString,
                )
        self.ImageRequest = channel.unary_unary(
                '/flask_grpc.FlaskService/ImageRequest',
                request_serializer=msg__pb2.ImageMessage.SerializeToString,
                response_deserializer=msg__pb2.ImageMessage.FromString,
                )


class FlaskServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StringRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NDArrayRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImageRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StringRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.StringRequest,
                    request_deserializer=msg__pb2.StringMessage.FromString,
                    response_serializer=msg__pb2.StringMessage.SerializeToString,
            ),
            'NDArrayRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.NDArrayRequest,
                    request_deserializer=msg__pb2.NDArrayMessage.FromString,
                    response_serializer=msg__pb2.NDArrayMessage.SerializeToString,
            ),
            'ImageRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ImageRequest,
                    request_deserializer=msg__pb2.ImageMessage.FromString,
                    response_serializer=msg__pb2.ImageMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flask_grpc.FlaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FlaskService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StringRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flask_grpc.FlaskService/StringRequest',
            msg__pb2.StringMessage.SerializeToString,
            msg__pb2.StringMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NDArrayRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flask_grpc.FlaskService/NDArrayRequest',
            msg__pb2.NDArrayMessage.SerializeToString,
            msg__pb2.NDArrayMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImageRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flask_grpc.FlaskService/ImageRequest',
            msg__pb2.ImageMessage.SerializeToString,
            msg__pb2.ImageMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)