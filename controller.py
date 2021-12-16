from node import node
from aloha_event import Send as Event
#from Event import Event
from Simulator import Simulator
from UniformDistribution import UniformDistribution
from RandTimeGenerator import RandTimeGenerator as rtg
class controller:
    def __init__(self, p_gen, p_send, nums, ep,T) :
        self.un=UniformDistribution()
        self.rtg=rtg()
        self.p_gen=p_gen
        self.p_send=p_send
        self.nums=nums
        self.node=node(nums)
        self.sim=Simulator()
        self.ep=ep
        self.el=[]
        self.T=T
        self.All=0
        self.success=0
        self.time=0

    def gen(self):
        #property=self.un.extract_01_number()
        property=self.rtg.dot_ud_time_generate(0.0,1.0)
        for ID in range(self.nums):
            if property < self.p_gen or self.node.get_status==1:
                self.node.gen_message(ID)
                gen=Event("gen", "B", ID, self.T)
                gen.ud_event_initialize("0",0,100)
                self.el.append(gen)
            
    def send(self):
        property=self.un.extract_01_number()
        for ID in range(self.nums):
            if property < self.p_send & self.node.get_status==1:
                self.node.send(ID)
            # addevent(id)

    def reset(self):
        success=self.sim.success_ID
        for x in success:
            self.node.send(x)
        self.el.clear()
        self.sim.success_ID.clear()
    
    def start(self):
        for i in range(self.ep):
            #print("epoch: "+str(i))
            self.gen()
            self.All+=self.el.__len__()
            self.sim.run(self.el)
            self.success+=self.sim.success_ID.__len__()
            self.time+=self.sim.current_time

            #print(self.sim.success_ID)
            self.reset()
    

