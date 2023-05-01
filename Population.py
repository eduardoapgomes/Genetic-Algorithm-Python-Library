import numpy as np
import random


class Population():
    """
    A population of binary strings used for genetic algorithms.
    Attributes:
        data (list): A list of binary strings representing the individuals in the population.
        size (int): The number of individuals in the population.
        number_of_bits (int): The number of bits in each binary string.
    Methods:
        __init__(self, population): Initializes a new instance of the Population class.
    """

    def __init__(self, population):
        self.data = population  # set population (list of binary strings)
        self.size = population  # set number of individuals from population
        self.number_of_bits = population  # set the number of bits of the first individual

    def __add__(self, population2):
        """
        Concatenates two instances of the Population class
        Args:
            Population(): a instance of the Population class
        Examples:
        new_population = Population(data1) + Population(data2)
        """
        return Population(self.data + population2.data)

    @property
    def data(self):
        """
        Get the list of binary strings representing the individuals in the population.
        Args:
            list: The list of binary strings representing the individuals in the population.
        """
        return self.__population

    @data.setter
    def data(self, population):
        self.__population = population
        return self

    @property
    def size(self):
        """
        Get the number of individuals in the population.
        Args:
            int: The number of individuals in the population.
        """
        return self.__population_size

    @size.setter
    def size(self, population):
        self.__population_size = len(population)
        return self

    @property
    def number_of_bits(self):
        """
        Set the number of bits for an individual from the population.
        Args:
            population (list): A list of binary strings representing the individuals in the population.
        """
        return self.__number_of_bits

    @number_of_bits.setter
    def number_of_bits(self, population):
        self.__number_of_bits = len(population[0])
        return self
