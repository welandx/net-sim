#!/usr/bin/env python3

from Event import Event as event
from node import node as nd
from controller import controller as cn

nums=10
epochs=10


control=cn(0.1,0.05,10,10)


def init_event():
    pass

def start_sim():
    pass

def end_sim():
    pass

for x in epochs:
    init_event()
    start_sim()
    end_sim()
