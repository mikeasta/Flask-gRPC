import logging 
import grpc
import settings
from concurrent import futures
from services.pb_handler import API_Server
from messages.msg_pb2_grpc import add_FlaskServiceServicer_to_server

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FlaskServiceServicer_to_server(API_Server, server)
    server.add_insecure_port(f'[::]:{settings.BACKEND_PORT}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()