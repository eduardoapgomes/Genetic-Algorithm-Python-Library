import random
import numpy
from Population import Population
from Fitness import Fitness


class Tournament:
    def __init__(self, selection, fitness, population):
        self.population = population.data
        self.selection = selection
        self.performance = fitness.performance
        self = self.compete()

    @property
    def new_population(self):
        new_population = random.sample(
            self.winner_list, self.selection.number_of_tournaments())
        return Population(new_population)

    def compete(self):
        for participants in self.selection.tournament_sample():
            self.participants = participants
            self.first_participant = self.participants
            self.second_participant = self.participants
            self.winner_list_performance = self.matchperformance()
            self.winner_list = self.winner()

    def winner(self):
        return self.population[self.who_is_winner]

    def matchperformance(self):
        return self.performance[self.who_is_winner]

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, new_participants):
        self.__participants = new_participants
        return self

    @property
    def winner_list_performance(self):
        return self.__winner_list_performance

    @winner_list_performance.setter
    def winner_list_performance(self, performance_of_winner):
        if hasattr(self, 'winner_list_performance') == False:
            self.__winner_list_performance = [performance_of_winner]
        else:
            self.__winner_list_performance.append(performance_of_winner)
            return self

    @property
    def winner_list(self):
        return self.__winner_list

    @winner_list.setter
    def winner_list(self, winner):
        if hasattr(self, 'winner_list') == False:
            self.__winner_list = [winner]
        else:
            self.__winner_list.append(winner)
        return self

    @property
    def first_participant(self):
        return self.__first_participant

    @first_participant.setter
    def first_participant(self, participants):
        self.__first_participant = self.performance[participants[0]]
        return self

    @property
    def second_participant(self):
        return self.__second_participant

    @second_participant.setter
    def second_participant(self, participants):
        self.__second_participant = self.performance[participants[1]]
        return self

    @property
    def who_is_winner(self):
        if self.first_participant < self.second_participant:
            return self.participants[0]
        else:
            return self.participants[1]
