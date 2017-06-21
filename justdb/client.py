import os
import zmq
import just


class JustDB():

    def __init__(self):
        # if not exist server, spawn server, try except around
        context = zmq.Context()

        # try to start server in background
        os.system("justdb serve &")

        main_socket = context.socket(zmq.REQ)
        main_socket.connect("tcp://localhost:5555")

        # print("Connecting to write server")
        freeze_socket = context.socket(zmq.REQ)
        freeze_socket.connect("tcp://localhost:6666")

        self.main_socket = main_socket
        self.freeze_socket = freeze_socket

    def execute(self, fn, *args, **kwargs):
        self.main_socket.send(b"")
        _ = self.main_socket.recv()
        return_value = None
        try:
            return_value = fn(*args, **kwargs)
        finally:
            self.freeze_socket.send(b"")
            _ = self.freeze_socket.recv()
        return return_value

    def read(self, fname, no_exist=None, unknown_type="RAISE"):
        return self.execute(just.read, fname, no_exist, unknown_type)

    def write(self, obj, fname, mkdir_no_exist=True, skip_if_exist=False):
        return self.execute(just.write, obj, fname, mkdir_no_exist, skip_if_exist)

    def remove(self, fname, no_exist=None):
        return self.execute(just.remove, fname, no_exist)

    def __getitem__(self, k):
        return self.read(k)

    def __setitem__(self, v, k):
        return self.write(k, v)
