import random
import numpy as np


class Selection():
    """
    A class for generating a tournament sample and calculating the number of tournaments and crossovers
    for a genetic algorithm.

    Args:
        population_size (int): The size of the population.
        pc (float): The percentage of crossovers, as a float between 0 and 1.
    """

    def __init__(self, population, pc):
        self = self.__set_population_size(population.size)
        self = self.__set_crossover_percentage(pc)
        self = self.__generate_tournament_sample()
        self = self.__calculate_selection_and_crossover_sample_size()

    def pc(self):
        """Returns the percentage of crossovers, divided by 2."""
        return self.__pc

    def population_size(self):
        """Returns the size of the population."""
        return int(self.__population_size)

    def tournament_sample(self):
        """Returns the tournament sample."""
        return self.__tournament_sample

    def number_of_tournaments(self):
        """Returns the number of tournaments to be conducted."""
        return int(self.__number_of_tournaments)

    def number_of_crossovers(self):
        """Returns the number of crossovers to be performed."""
        return int(self.__number_of_crossovers)

    def __set_population_size(self, population_size):
        """Sets the size of the population."""
        self.__population_size = int(population_size)
        return self

    def __set_crossover_percentage(self, pc):
        """Sets the percentage of crossovers, divided by 2."""
        self.__pc = pc/2
        return self

    def __generate_tournament_sample(self):
        """Generates the tournament sample."""
        sample = random.sample(
            range(self.population_size()), self.population_size())
        self.__tournament_sample = np.stack(
            (sample[:-1:2], sample[1::2]), axis=1)
        return self

    def __tournament_size(self):
        """Returns the size of the tournament sample."""
        return len(self.tournament_sample())

    def __calculate_selection_and_crossover_sample_size(self):
        """Calculates the number of tournaments and crossovers."""
        self = self.__initialize_crossover_sample_size()
        self = self.__initialize_tournaments_sample_size()
        self = self.__correct_sample_size()
        return self

    def __initialize_crossover_sample_size(self):
        """Initializes the number of crossovers."""
        self.__number_of_crossovers = np.round(
            self.population_size() * (1 - self.pc()), 0)
        return self

    def __initialize_tournaments_sample_size(self):
        """Initializes the number of tournaments."""
        self.__number_of_tournaments = self.population_size() - self.__number_of_crossovers
        return self

    def __correct_sample_size(self):
        """Corrects the number of tournaments and crossovers."""
        while self.__number_of_tournaments > self.__tournament_size():
            self.__number_of_tournaments -= 1
            self.__number_of_crossovers += 1
            return self
