from RandTimeGenerator import RandTimeGenerator
from NormalDistribution import NormalDistribution
from datetime import datetime


class Event:
    def __init__(self, event_type):
        self.event_id = None
        self.type = event_type
        self.event_date = None
        self.event_state = None
        self.duration = None
        self.next_event = None

    def ud_event_initialize(self, event_state, x, y):
        temp = NormalDistribution()
        seed = datetime.now().microsecond
        temp.initialize_generator(seed)
        self.event_id = temp.extract_number()
        del temp

        self.event_state = event_state

        self.event_date = RandTimeGenerator().ud_time_generate(x, y)

    def nd_event_initialize(self, event_state, miu, sigma):
        temp = NormalDistribution()
        seed = datetime.now().microsecond
        temp.initialize_generator(seed)
        self.event_id = temp.extract_number()
        del temp

        self.event_state = event_state

        self.event_date = RandTimeGenerator().nd_time_generate(miu, sigma)

    def event_change_state(self, new_state):
        self.event_state = new_state



