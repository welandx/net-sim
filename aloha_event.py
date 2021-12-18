#!/usr/bin/env python3
from Event import Event


class Send(Event):
    def __init__(self, event_name, event_type, event_nums, T):
        super().__init__(event_name, event_type, event_nums)
        self.T = T

    def run(self, current_time, next_time, next_next_time):
        T = self.T
        if next_next_time - next_time > T and next_time - current_time > T:
            self.event_state = "Success"
            print("node : " + str(self.event_nums) +
                  " send "+str(self.event_state))
            return self.event_state
        else:
            self.event_state = "Failed"
            print("node : " + str(self.event_nums) +
                  " send "+str(self.event_state))
            return self.event_state

class reSend(Event):
    def __init__(self, event_name, event_type, event_nums, T):
        super().__init__(event_name, event_type, event_nums)
        self.T = T

    def run(self, current_time, next_time, next_next_time):
        T = self.T
        if next_next_time - next_time > T and next_time - current_time > T:
            self.event_state = "Success"
            print("node : " + str(self.event_nums) +
                  " resend "+str(self.event_state))
            return self.event_state
        else:
            self.event_state = "Failed"
            print("node : " + str(self.event_nums) +
                  " resend "+str(self.event_state))
            return self.event_state


class Gen(Event):
    def __init__(self, event_name, event_type, event_nums):
        super().__init__(event_name, event_type, event_nums)
        self.message = ""
