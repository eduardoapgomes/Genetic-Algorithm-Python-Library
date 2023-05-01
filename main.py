from mimetypes import init
from operator import le
from Population import Population
from Selection import Selection
from Individuals import Individuals
from Cutpoint import Cutpoint
from Crossover import Crossover
from Mutation import Mutation
from Tournament import Tournament
from Fitness import Fitness
import numpy as np
import random


Xb = ['01010011100',  # population
      '11111101010',
      '01110110110',
      '11010110111']


def fitness(data):
    return 525


Pc = 0.4
Pm = 0.01
performance = [0.1, 0.7, 0.9, 1.0]


population = Population(Xb)
selection = Selection(population, Pc)
tournament = Tournament(selection, performance, population)
crossover = Crossover(population, selection)

# Atualizando a população(torneio, crossover e mutation)
tournament = tournament.new_population
crossover = crossover.new_population
mutants = Mutation(Pm, crossover)
mutants = mutants.new_population
# Nova geração
new_population = tournament + mutants


print(new_population)
