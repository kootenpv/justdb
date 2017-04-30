import zmq
import sys


def create_server():
    context = zmq.Context()

    try:
        main_socket = context.socket(zmq.REP)
        main_socket.bind("tcp://*:5555")

        freeze_socket = context.socket(zmq.REP)
        freeze_socket.bind("tcp://*:6666")
    except zmq.error.ZMQError:
        print("JustDB already running")
        sys.exit()

    while True:
        _ = main_socket.recv()
        main_socket.send(b"")

        _ = freeze_socket.recv()
        freeze_socket.send(b"")
