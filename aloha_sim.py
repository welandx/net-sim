#!/usr/bin/env python3

from numpy.lib.function_base import average
from controller import controller as cn
from numpy import exp

nums = 15
epochs = 100
p_gen = 0.7
p_send = 0.5
T = 0.15 

control = cn(p_gen, p_send, nums, epochs, T)
control.start()

All = control.All
success=control.success
time = control.time
m_re=control.get_resend()
averageDelay=control.get_delay()

G = (All-(control.gennum-success))/time*T
Si=success/time*T
S = G*exp(-2*G)

print("total send: " + str(All))
print("total time: "+str(time))
print("G is: "+str(G))
print("Si is: "+str(Si))
print("S is: "+str(S))
print("average resent times: "+str(m_re))
print("average detention: "+str(averageDelay))
