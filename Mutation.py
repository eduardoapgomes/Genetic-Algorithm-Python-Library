import random


class Mutation:
    def __init__(self, Pm, population):
        self.Pm = Pm
        self.population = population.data
        self.Nbits = population.number_of_bits

    def new_population(self):
        new_population = []
        for individual in self.population:
            self = self.random_mutant()
            #self.mutation_list
            if self.any_mutation():
                mutant = self.bitflip(individual, self.mutation_list)# o que acontece quando mutation list nao existe ou é vazio?
                new_population.append(mutant)
                del self.mutation_list
            else:
                new_population.append(individual)
        return new_population
        
    def any_mutation(self):
        if hasattr(self,'mutation_list')==True:
            return True
        else:
            return False

    def random_mutant(self):
        # del self.mutation_list
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
        if hasattr(self, 'mutation_list') == False:
            self.__mutation_list = [index]
        else:
            self.__mutation_list.append(index)
        return self

    @ mutation_list.deleter
    def mutation_list(self):
        if hasattr(self, 'mutation_list') == True:
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
