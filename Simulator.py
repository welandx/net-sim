from Event import Event
from NormalDistribution import NormalDistribution
import time
from RandTimeGenerator import RandTimeGenerator

class Simulator:
    def __init__(self):
        self.event_dict = {}
        self.event_list = []
        self.current_time = 0
        self.next_time = None
        self.next_next_time = None
        self.total_time = 0
        self.due_now_list = []

    def add_event(self,event):
        self.event_dict[event] = event.event_date
        print("Add a new event:" + event.event_name )
        print("*** Event ID: " + str(event.event_id))
        print("+++ Event Type: " + event.event_type)
        print("----------------------")

    def arrange_event(self):
        sorted(self.event_dict.items(), key = lambda kv:(kv[1], kv[0]))
        self.event_list = list(self.event_dict)

    def a_phrase(self):
        self.current_time = 0 # 从零开始

        self.next_time = self.event_list[0].event_date
        # 此时就得到了最近的时间

        self.due_now_list.clear()

        for temp in self.event_dict:
            if temp.event_date == self.next_time:
                self.due_now_list.append(temp)
            if temp.event_date > self.next_time:
                self.next_next_time = temp.event_date
                break

        for temp in self.due_now_list:
            self.event_dict.pop(temp)

        return self.next_time

    def b_phrase(self, *event):
        self.current_time = event.event_date
        event.run()

    def c_pharese(self, *event):
        self.current_time = event.event_date
        event.run()
        print("C Phrase")




