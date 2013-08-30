#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#
import sys
import time
import zmq

context = zmq.Context()

#  Socket to talk to server
print "Connecting to hello world server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:5555")

while True:
    socket.send(sys.argv[2])

    #  Get the reply.
    message = socket.recv()
    print "Received reply ", "[", message, "]"

    time.sleep(float(sys.argv[1]))
