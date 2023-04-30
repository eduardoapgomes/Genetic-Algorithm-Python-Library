import numpy as np
import random


class Cutpoint():
    def __init__(self, number_of_bits):
        self.random_cutpoint = number_of_bits

    @property
    def random_cutpoint(self):
        return self.__random_cutpoint

    @random_cutpoint.setter
    def random_cutpoint(self, number_of_bits):
        self.__random_cutpoint = random.randint(0, number_of_bits-1)
        return self
