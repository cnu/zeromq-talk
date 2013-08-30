import sys
import time
import json
import zmq

import requests
from lxml import etree

def get_title(url):
    """Given a XKCD url, retrieve the title of the image."""
    r = requests.get(url)
    tree = etree.HTML(r.content)
    title = tree.xpath('//div[@id="comic"]/img/@title')
    if title:
        return title[0]
    else:
        return None

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

# Process tasks forever
while True:
    s = receiver.recv()
    title = get_title(s)
    print s, title

    # Send a JSON payload to sink
    sender.send(json.dumps({"url":s, "title":title}))