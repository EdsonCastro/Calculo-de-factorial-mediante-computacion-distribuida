#!/usr/bin/python2

import zmq
import sys

def get_fac(num):
    # Set up the zeromq context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    socket.connect('tcp://127.0.0.1:4545')
    socket.send(num)

    total = int(socket.recv())
    print total

if __name__ == '__main__':
    get_fac(sys.argv[1])