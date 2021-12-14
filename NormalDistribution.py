from UniformDistribution import UniformDistribution
import math


class NormalDistribution(UniformDistribution):

    def standard_normal_distribution(self):
        x1 = self.extract_01_number()
        x2 = self.extract_01_number()
        return math.sqrt(-2 * math.log(x1)) * math.cos(2 * math.pi * x2)

    def normal_distribution(self, miu, sigma):
        z1 = self.standard_normal_distribution()
        return z1*sigma+miu
