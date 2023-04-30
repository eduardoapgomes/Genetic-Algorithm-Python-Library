from Population import Population
from Individuals import Individuals
from Cutpoint import Cutpoint
import numpy as np
import random


class Crossover():
    def __init__(self, population, selection):
        # super().__init__(population)
        # Population
        self.population = population
        self.number_of_crossingovers = selection.number_of_crossovers()

    @property
    def new_population(self):
        self = self.reproduce()  # generate a new population of individuals
        return self.__new_population

    @property
    def number_of_crossingovers(self):
        return self.__number_of_crossingovers

    @number_of_crossingovers.setter
    def number_of_crossingovers(self, number_of_crossing_over):
        self.__number_of_crossingovers = number_of_crossing_over
        return self

    def reproduce(self):
        self.__new_population = [self.crossover_individuals()
                                 for k in range(self.number_of_crossingovers)]
        return self

    def crossover_individuals(self):
        self.individuals = self.population.data
        self.cutpoint = self.population.number_of_bits
        self.new_individual = self.gen_individual
        return self.new_individual

    @property
    def gen_individual(self):
        return self.individuals.first[0:self.cutpoint.random_cutpoint]+self.individuals.second[self.cutpoint.random_cutpoint:]

    @property
    def individuals(self):
        return self.__individuals

    @individuals.setter
    def individuals(self, population):
        self.__individuals = Individuals(population)

    @property
    def cutpoint(self):
        return self.__cutpoint

    @cutpoint.setter
    def cutpoint(self, number_of_bits):
        self.__cutpoint = Cutpoint(number_of_bits)

    @property
    def new_individual(self):
        return self.__new_individual

    @new_individual.setter
    def new_individual(self, individual):
        self.__new_individual = individual
        return self
