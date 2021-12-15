#!/usr/bin/env python3

from Event import Event as event
from node import node as nd
from controller import control_node as cn
nums=10
epochs=10

gen_message = event(B)
send = event(C)

node=nd(10)

def init_event():
    for i in nums:
        node.gen_message(i)
        if node.get_status(i) == 1 :
            pass
        node.send(i)
    
    pass

def start_sim():
    pass

def end_sim():
    pass

for x in epochs:
    init_event()
    start_sim()
    end_sim()
