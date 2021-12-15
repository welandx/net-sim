from Event import Event
from NormalDistribution import NormalDistribution
import time
from RandTimeGenerator import RandTimeGenerator

class Simulator:
    def __init__(self):
        self.event_list = {}
        self.start_time = 0
        self.next_time = None
        self.total_time = 0
        self.due_now_list = []

    def add_event(self,event):
        self.event_list[event] = event.event_date
        print("Add a new event:" + event.event_name )
        print("*** Event ID: " + str(event.event_id))
        print("+++ Event Type: " + event.event_type)
        print("----------------------")

    def arrange_event(self):
        sorted(self.event_list.items(), key = lambda kv:(kv[1], kv[0]))

    def a_phrase(self):
        self.start_time = 0 # 从零开始

        temp_list = list(self.event_list)
        self.next_time = temp_list[0].event_date
        del temp_list
        # 此时就得到了最近的时间

        self.due_now_list.clear()

        for temp in self.event_list:
            if temp.event_date == self.next_time:
                self.due_now_list.append(temp)

        for temp in self.due_now_list:
            self.event_list.pop(temp)
        return self.next_time

    def b_phrase(self):


    def c_phrase(self):
        print()
c = Event("tcp","tcp","1")
c.ud_event_initialize("0",1639558635,1639559635)
d = Event("tcp1","tcp","1")
d.ud_event_initialize("0",1639568635,1639569635)
sim = Simulator()
sim.add_event(c)
sim.add_event(d)
sim.arrange_event()
sim.a_phrase()

print("1231")