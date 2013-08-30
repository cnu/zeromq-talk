#
#   Stock update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects stock updates and prints it
#

import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print "Collecting updates from stock server..."
socket.connect ("tcp://localhost:5556")


scrip_filter = sys.argv[1:] if len(sys.argv) > 1 else ["AAPL"]
for scrip in scrip_filter:
    socket.setsockopt(zmq.SUBSCRIBE, scrip)


while True:
    string = socket.recv()
    stock, price = string.split()
    print "%s: %s" %(stock, price)
