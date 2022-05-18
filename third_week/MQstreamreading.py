import numpy as np 
import zmq
import array
Nt=1024
context=zmq.Context()
socket=context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5556")
socket.setsockopt_string(zmq.SUBSCRIBE,b'')
vector1=[]
while (len(vector1)<Nt):
    raw_recv=socket.recv()
    recv=array.array('1',raw_recv)
    print(recv)