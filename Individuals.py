import numpy as np
import random


class Individuals():
    def __init__(self, population):
        self.random_pair = population
        self.first = self.random_pair
        self.second = self.random_pair

    @property
    def random_pair(self):
        return self.__individuals_pair

    @random_pair.setter
    def random_pair(self, population):
        self.__individuals_pair = random.sample(population, 2)
        return self

    @property
    def first(self):
        return self.__first_individual

    @first.setter
    def first(self, individuals_pair):
        self.__first_individual = individuals_pair[0]
        return self

    @property
    def second(self):
        return self.__second_individual

    @second.setter
    def second(self, individuals_pair):
        self.__second_individual = individuals_pair[1]
        return self
