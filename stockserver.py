#
#   Stock Ticker server
#   Binds PUB socket to tcp://*:5556
#   Publishes random stock updates
#

import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")
scrips = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

while True:
    scrip = random.choice(scrips)
    price = random.randrange(20,700)

    msg = "%s: %d" % (scrip, price)
    print msg
    socket.send(msg)
    time.sleep(0.5)