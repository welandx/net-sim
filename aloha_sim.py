#!/usr/bin/env python3

from Event import Event as event
from node import node as nd
from controller import controller as cn

nums=10
epochs=10


control=cn(0.7,0.5,20,8)

control.start()


