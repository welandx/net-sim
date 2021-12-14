from NormalDistribution import NormalDistribution
from datetime import datetime


class RandTimeGenerator:
    def __init__(self):
        self.seed = datetime.now().microsecond
        self.nd_time_initialize = NormalDistribution()
        self.nd_time_initialize.initialize_generator(self.seed)

    def nd_time_generate(self, miu, sigma):
        return round(self.nd_time_initialize.normal_distribution(miu,sigma))

    def nd_time_generate(self):
        return round(self.nd_time_initialize.standard_normal_distribution())

    def ud_time_generate(self,x,y):
        return  round(self.nd_time_initialize.extract_xy_number(x,y))