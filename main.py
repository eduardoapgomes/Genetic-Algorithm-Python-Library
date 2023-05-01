from math import inf
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
import matplotlib.pyplot as plt


def minimize(data):
    # Função de minimização
    return -int(data, 2)/255


Pc = 0.6   # probabilidade de crossover
Pm = 0.01  # probabilidade de mutação

# Definindo a função fitness
fitness = Fitness(minimize)

# Gerando a população inicial e desempenho inicial
population = Population.generate(100, 8)
performance = fitness.evaluate(population)

# Algoritmo Genético
iter = 0
x_opt = np.inf
while iter < 1000:
    # Parametrizando operações do AG
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
    performance = fitness.evaluate(new_population)

    # Solução ótima
    x_arg_min = np.argmin(performance)
    if performance[x_arg_min] < x_opt:
        x_opt, x_min = performance[x_arg_min], new_population.data[x_arg_min]

    # proxima iteração
    population = new_population
    iter += 1
