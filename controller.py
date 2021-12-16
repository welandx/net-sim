from node import node
from Event import Send as Event
from Simulator import Simulator
from UniformDistribution import UniformDistribution
class controller:
    def __init__(self, p_gen, p_send, nums, ep) :
        self.un=UniformDistribution()
        self.p_gen=p_gen
        self.p_send=p_send
        self.node=node(nums)
        self.sim=Simulator()
        self.ep=ep

    def gen(self, ID):
        property=self.un.extract_01_number()
        if property < self.p_gen & self.node.get_status!=1:
            self.node.gen_message(ID)
            gen=Event("gen", 1, ID)
            self.sim.add_event(gen)
            
    def send(self):
        property=self.un.extract_01_number()
        if property < self.p_send & self.node.get_status==1:
            self.node.send()
            # addevent(id)

    def reset(self):
        success=sim.getsuccess()
        for x in success:
            self.node.send(x)
    
    def start(self):
        for i in self.ep:
            gen()
            self.sim.a_phrase()
            reset()
    

