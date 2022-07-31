import logging 
import grpc
from settings import BACKEND_PORT
from concurrent import futures
from pb_handler import API_Server
from msg_pb2_grpc import add_FlaskServiceServicer_to_server

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FlaskServiceServicer_to_server(API_Server(), server)
    server.add_insecure_port(f'[::]:{BACKEND_PORT}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print(f'Server on port {BACKEND_PORT} is running!')
    logging.basicConfig()
    serve()
    print('Server terminated!')