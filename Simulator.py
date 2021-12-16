from Event import Event
from NormalDistribution import NormalDistribution
import time
from RandTimeGenerator import RandTimeGenerator

class Simulator:
    def __init__(self):
        self.event_dict = {}
        self.event_list = []
        self.temp_dict = {}
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
        print("*** Event ID: " + str(event.event_nums))
        print("+++ Event Type: " + event.event_type)
        print("event date")
        print(event.event_date)
        print("----------------------")


    def arrange_event(self):
        self.event_list = sorted(self.event_dict.items(), key=lambda x: x[1], reverse=False)


    def a_phrase(self):
        self.event_list = list(self.event_list)
        self.next_time = self.event_list[0][0].event_date
        # 此时就得到了最近的时间

        self.due_now_list.clear()


        for temp in self.event_list:
            if temp[0].event_date == self.next_time:
                self.due_now_list.append(temp[0])
            if temp[0].event_date > self.next_time:
                self.next_next_time = temp[0].event_date
                break

        for temp in self.due_now_list:
            self.event_dict.pop(temp)


        return self.due_now_list

    def cal_success_times(self,phrase,event_state):
        if phrase == "C" and event_state == "Success":
            self.c_phrase_success += 1
        elif phrase == "B" and event_state == "Success":
            self.b_phrase_success += 1
            self.success_ID.append(event.event_nums)

    def b_phrase(self , *event_list):
        for temp in event_list:
            self.current_time = temp[0].event_date
            self.due_c_list.append(temp[0].run())
            '''
            这里我想要返回值为事件
            然后逐一添加到C要做里面
            '''
            print(temp[0].event_state)
            self.cal_success_times("B", temp[0].event_state)
        self.due_now_list.clear()

    def c_pharese(self, *event_list):
        print("C phrase")
        for temp in event_list:
            self.current_time = temp[0].event_date
            temp[0].run()
            self.cal_success_times("C", temp[0].event_state)
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


Sim = Simulator()
a = Event("TCP","TCP",0)
b = Event("TCP1","TCP",1)

a.ud_event_initialize("0",1,100)
b.ud_event_initialize("0",101,200)

c  = [b,a]

Sim.run(c)





