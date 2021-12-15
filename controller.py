from node import node
from event import event
from UniformDistribution import UniformDistribution
class control_node:
    def __init__(self, p_gen, p_send, nums) :
        self.un=UniformDistribution()
        self.p_gen=p_gen
        self.p_send=p_send
        self.node=node(nums)

    def gen(self, ID):
        property=self.un.extract_01_number()
        if property < self.p_gen & self.node.get_status!=1:
            self.node.gen_message(ID)
            # addevent(id)
    def send(self):
        property=self.un.extract_01_number()
        if property < self.p_send & self.node.get_status==1:
            self.node.send()
            # addevent(id)