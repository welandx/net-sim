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
        self.due_c_list = []
        self.b_phrase_success = 0
        self.c_phrase_success = 0
        self.success_ID=[]

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

        return self.due_now_list

    def cal_success_times(self,phrase,*event):
        if phrase == "C" and event.event_state == "Success":
            self.c_phrase_success += 1
        elif phrase == "B" and event.event_state == "Success":
            self.b_phrase_success += 1
            self.success_ID.pop(event.event_nums)

    def b_phrase(self, *event_list):
        for temp in event_list:
            self.current_time = temp.event_date
            self.due_c_list.append(temp.run())
            '''
            这里我想要返回值为事件
            然后逐一添加到C要做里面
            '''
            self.cal_success_times("B", temp)
        self.due_now_list.clear()

    def c_pharese(self, *event_list):
        print("C phrase")
        for temp in event_list:
            self.current_time = temp.event_date
            temp.run()
            self.cal_success_times("C", temp)
        self.due_c_list.clear()

    def run(self,event_list):
        for i in event_list:
            self.add_event(i)
        self.arrange_event()
        while len(self.event_dict) != 0:
            self.a_phrase()
            print(self.current_time)
            print(self.next_time)

            self.b_phrase(self.due_now_list)
            print(self.current_time)
            print(self.next_time)
            print(self.b_phrase_success)

            self.c_pharese(self.due_c_list)
            print(self.current_time)
            print(self.next_time)
            print(self.c_phrase_success)






