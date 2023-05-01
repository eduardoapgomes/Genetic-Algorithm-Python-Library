import random
import numpy as np


class Fitness:
    def __init__(self, function):
        self.function = function

    def evaluate(self, population):
        self.performance = population
        self.argmin = self.performance
        if self.is_minimizing():
            self.min = self.performance
            self.xmin = population
        return self

    @property
    def performance(self):
        return self.__performance

    @performance.setter
    def performance(self, population):
        self.__performance = [self.function(individual)
                              for individual in population.data]

    @property
    def xmin(self):
        return self.__xmin

    @xmin.setter
    def xmin(self, population):
        self.__xmin = population.data[self.argmin]

    @property
    def argmin(self):
        return self.__argmin

    @argmin.setter
    def argmin(self, performance):
        self.__argmin = np.argmin(performance)
        return self

    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, performance):
        self.__min = performance[self.argmin]

    def is_minimizing(self):
        if hasattr(self, 'min') == False:
            return True
        else:
            if self.performance[self.argmin] <= self.min:
                return True
            else:
                return False

    # def argmin(self, performance):
    #    x_arg_min = np.argmin(performance)
        # if performance[x_arg_min] < x_opt:
        #    x_opt, x_min = performance[x_arg_min], new_population.data[x_arg_min]
