from node import node
from aloha_event import Send as Event, reSend
from aloha_event import reSend as rs

#from Event import Event
from Simulator import Simulator
from UniformDistribution import UniformDistribution
from RandTimeGenerator import RandTimeGenerator as rtg


class controller:
    def __init__(self, p_gen, p_send, nums, ep, T):
        self.un = UniformDistribution()
        self.rtg = rtg()
        self.p_gen = p_gen
        self.p_send = p_send
        self.nums = nums
        self.node = node(nums)
        self.sim = Simulator()
        self.ep = ep
        self.el = []
        self.T = T
        self.All = 0
        self.success = 0
        self.time = 0
        self.rsnum=0
        self.gennum=0
        self.delay=0.0
        self.curtime=0

    def gen(self):
        # property=self.un.extract_01_number()
        property = self.rtg.dot_ud_time_generate(0.0, 1.0)
        for ID in range(self.nums):
            if self.node.get_status(ID) == 1:
                resend=rs("resend","B", ID,self.T)
                resend.ud_event_initialize("0",0,10000,4000)
                self.el.append(resend)
                self.rsnum+=1
                self.node.set_detention(ID,self.sim.current_time)
            if property < self.p_gen and self.node.get_status(ID) != 1:
                self.node.gen_message(ID)
                gen = Event("gen", "B", ID, self.T)
                gen.ud_event_initialize("0", 0, 10000,4000)
                self.el.append(gen)
                self.gennum+=1
                self.node.set_time(ID,self.sim.current_time)

    def send(self):
        property = self.un.extract_01_number()
        for ID in range(self.nums):
            if property < self.p_send and self.node.get_status == 1:
                resend=reSend("resend","B", ID,self.T)
            # addevent(id)

    def reset(self):
        success = self.sim.success_ID
        for x in success:
            self.node.send(x)
        self.el.clear()
        self.sim.success_ID.clear()
    
    def get_resend(self):
        return self.rsnum/self.gennum
    
    def get_delay(self):
        self.delay= sum(self.node.detention)/self.success
        return self.delay

    def start(self):
        for i in range(self.ep):
            #print("epoch: "+str(i))
            self.gen()
            self.All += self.el.__len__()
            self.sim.run(self.el)
            self.success += self.sim.success_ID.__len__()
            self.time += self.sim.current_time

            # print(self.sim.success_ID)
            self.reset()
