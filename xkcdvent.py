import sys
import zmq

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

print "Press Enter when the workers are ready: "
_ = raw_input()
print "Sending tasks to workers..."

base_url = 'http://xkcd.com/'
urls = [base_url + str(i) for i in xrange(1, int(sys.argv[1]))]

for url in urls:
    sender.send(url)