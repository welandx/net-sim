#!/usr/bin/env python3

from controller import controller as cn
from numpy import exp

nums = 25
epochs = 100
p_gen = 0.7
p_send = 0.5
T = 1

control = cn(p_gen, p_send, nums, epochs, T)
control.start()

All = control.All
time = control.time

G = All/time*T
S = G*exp(-2*G)

print("total send: " + str(All))
print("total time: "+str(time))
print("G is: "+str(G))
print("S is: "+str(S))
