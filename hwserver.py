#
#   Hello World Server in Python
#   Binds a REP socket to tcp://*:5555
#   Received "Hello" from client, replies with "World"
#

import zmq

context = zmq.Context()

print "Starting hello world server..."
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print "Got: ", message

    #  Send the reply.
    socket.send ("World")