from node import node
#from Event import Send as Event
from Event import Event
from Simulator import Simulator
from UniformDistribution import UniformDistribution
class controller:
    def __init__(self, p_gen, p_send, nums, ep) :
        self.un=UniformDistribution()
        self.p_gen=p_gen
        self.p_send=p_send
        self.nums=nums
        self.node=node(nums)
        self.sim=Simulator()
        self.ep=ep
        self.el=[]

    def gen(self):
        property=self.un.extract_01_number()
        for ID in range(self.nums):
            if property < self.p_gen or self.node.get_status==1:
                self.node.gen_message(ID)
                gen=Event("gen", "B", ID)
                gen.ud_event_initialize("0",ID,100)
                self.el.append(gen)
            
    def send(self):
        property=self.un.extract_01_number()
        if property < self.p_send & self.node.get_status==1:
            self.node.send()
            # addevent(id)

    def reset(self):
        success=self.sim.success_ID
        for x in success:
            self.node.send(x)
    
    def start(self):
        for i in range(self.ep):
            self.gen()
            self.sim.run(self.el)
            self.reset()
    

