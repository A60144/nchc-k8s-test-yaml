import time
import mxnet as mx
a = mx.nd.ones((2,3), mx.gpu())
print (a*2)
while True:
    time.sleep(5)
