import random
import numpy


class Fitness:
    def __init__(self, function):
        self.function = function

    def evaluate(self, population):
        return [self.function(individual) for individual in population.data]
