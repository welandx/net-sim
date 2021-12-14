'''

Description: Based on the pseudocode in https://en.wikipedia.org/wiki/Mersenne_Twister. 
             Generates uniformly distributed 32-bit integers in the range [0, 232 − 1] with the MT19937 algorithm
'''


class UniformDistribution:

    def __init__(self):
        self.MT = [0 for i in range(624)]
        self.index = 0

        # To get last 32 bits
        self.bitmask_1 = (2 ** 32) - 1

        # To get 32. bit
        self.bitmask_2 = 2 ** 31

        # To get last 31 bits
        self.bitmask_3 = (2 ** 31) - 1

    def initialize_generator(self,seed):
        self.MT[0] = seed
        for i in range(1, 624):
            self.MT[i] = ((1812433253 * self.MT[i - 1]) ^ ((self.MT[i - 1] >> 30) + i)) & self.bitmask_1

    def generate_numbers(self):
        "Generate an array of 624 untempered numbers"
        for i in range(624):
            y = (self.MT[i] & self.bitmask_2) + (self.MT[(i + 1) % 624] & self.bitmask_3)
            self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.MT[i] ^= 2567483615

    def extract_number(self):
        if self.index == 0:
            self.generate_numbers()
        y = self.MT[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 2636928640
        y ^= (y << 15) & 4022730752
        y ^= y >> 18

        self.index = (self.index + 1) % 624
        return y

    def extract_01_number(self):
        c = self.extract_number()
        return c/(2**32-1)
