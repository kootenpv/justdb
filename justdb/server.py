import sys
import zmq


def create_server():
    context = zmq.Context()

    try:
        main_socket = context.socket(zmq.REP)
        main_socket.bind("tcp://*:5555")

        freeze_socket = context.socket(zmq.REP)
        freeze_socket.bind("tcp://*:6666")
    except zmq.error.ZMQError:
        print("JustDB already running, this is no error.")
        sys.exit()

    print("Successfully started \033[92mjustdb\033[0m")
    while True:  # pragma: no cover
        _ = main_socket.recv()
        main_socket.send(b"")

        _ = freeze_socket.recv()
        freeze_socket.send(b"")
