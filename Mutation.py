import random
from Population import Population


class Mutation:
    def __init__(self, Pm, population):
        self.Pm = Pm
        self.population = population.data
        self.Nbits = population.number_of_bits

    @property
    def new_population(self):
        for individual in self.population:
            self = self.random_mutant()
            if self.any_mutation():
                self.mutant = individual
                self.individuals_list = self.mutant
                del self.mutation_list
            else:
                self.individuals_list = individual
        return Population(self.individuals_list)

    @property
    def mutant(self):
        return self.__mutant

    @mutant.setter
    def mutant(self, individual):
        self.__mutant = self.bitflip(individual, self.mutation_list)

    @property
    def individuals_list(self):
        return self.__individuals_list

    @individuals_list.setter
    def individuals_list(self, individual):
        if self.any_individual():
            self.__individuals_list.append(individual)
        else:
            self.__individuals_list = [individual]
        return self

    def any_individual(self):
        if hasattr(self, 'individuals_list'):
            return True
        else:
            return False

    def any_mutation(self):
        if hasattr(self, 'mutation_list') == True:
            return True
        else:
            return False

    def random_mutant(self):
        for bit_pointer in range(self.Nbits):
            if self.is_to_mutate_this_bit():
                self.mutation_list = bit_pointer
        return self

    def is_to_mutate_this_bit(self):
        if random.random() <= self.Pm:
            return True
        else:
            return False

    @ property
    def mutation_list(self):
        return self.__mutation_list

    @ mutation_list.setter
    def mutation_list(self, index):
        if self.any_mutation():
            self.__mutation_list.append(index)
        else:
            self.__mutation_list = [index]
        return self

    @ mutation_list.deleter
    def mutation_list(self):
        if self.any_mutation():
            del self.__mutation_list
        return self

    def bitflip(self, individual, pointer_list):
        self.individual = individual
        for pointer in pointer_list:
            self.bit = self.individual[pointer]
            if self.is_bit_zero():
                self.individual[pointer] = '1'
            if self.is_bit_one:
                self.individual[pointer] = '0'
        return ''.join(self.individual)

    @ property
    def bit(self):
        return self.__bit

    @ bit.setter
    def bit(self, abitstring):
        self.__bit = abitstring
        return self

    @ property
    def individual(self):
        return self.__individual

    @ individual.setter
    def individual(self, abinarystring):
        self.__individual = list(abinarystring)
        return self

    def is_bit_zero(self):
        if self.bit == '0':
            return True
        else:
            return False

    def is_bit_one(self):
        if self.bit == '1':
            return True
        else:
            return False
