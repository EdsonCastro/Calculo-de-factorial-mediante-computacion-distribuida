# File Transfer model #3
#
# In which the client requests each chunk individually, using
# command pipelining to give us a credit-based flow control.

import os
from threading import Thread

import zmq

from zhelpers import socket_set_hwm, zpipe

CHUNK_SIZE = 250000


# .split File server thread
# The server thread waits for a chunk request from a client,
# reads that chunk and sends it back to the client:

def server_thread(ctx):
    file = open("outputNotas.json", "r")

    router = ctx.socket(zmq.ROUTER)

    router.bind("tcp://*:6000")

    while True:
        # First frame in each message is the sender identity
        # Second frame is "fetch" command
        try:
            msg = router.recv_multipart()
        except zmq.ZMQError as e:
            if e.errno == zmq.ETERM:
                return   # shutting down, quit
            else:
                raise

        identity, command, offset_str, chunksz_str = msg

        assert command == b"fetch"

        offset = int(offset_str)
        chunksz = int(chunksz_str)

        # Read chunk of data from file
        file.seek(offset, os.SEEK_SET)
        data = file.read(chunksz)

        # Send resulting chunk to client
        router.send_multipart([identity, data])

# The main task is just the same as in the first model.
# .skip

def main():

    # Start child threads
    ctx = zmq.Context()
    a,b = zpipe(ctx)
    
    server = Thread(target=server_thread, args=(ctx,))
    server.start()

    # loop until client tells us it's done
    try:
        print a.recv()
    except KeyboardInterrupt:
        pass
    del a,b
    ctx.term()

if __name__ == '__main__':
    main()
