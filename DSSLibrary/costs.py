import py_dss_interface
import pandas as pd
import seaborn as sns
import numpy as np

from DSSLibrary.pythondss import *
from DSSLibrary.modeling import *
from DSSLibrary.costs import *


def start_dss():
    dss = py_dss_interface.DSSDLL()
    return dss

class system_costs():
    def __init__(self):
        # circuit_model is a function
        self = self.__set_cost_matrix()
        self = self.__set_start_dss()
        self = self.__set_default_lines()
        self = self.__set_default_lineloss_df()

    def CostMatrix(self):
        return self.__cost_matrix

    def DefaulLines(self):
        return self.__default_lines

    def DefaultLineLossDF(self):
        return self.__default_lineloss_df

    def DSS(self):
        return self.__start_dss

    def objective_function(self, lines):
        c1 = self.cost_of_cable_change(lines)
        c2 = self.constraint_adjacent_cable(lines)
        c3 = self.circuit_loss_cost(lines)
        costs = c1 + c2 + c3
        return costs

    def cost_of_cable_change(self, lines):
        # print(lines)
        default_lines = self.DefaulLines()
        cost_matrix = self.CostMatrix()
        N = len(default_lines)
        costs = []
        for k in range(N):
            m = default_lines[k]-1
            n = lines[k]-1  # line position [0 to N], i.e [1 to 5]

            if self.is_feasible_iter(m, n) == True:
                costs.append(cost_matrix[m, n])
            else:
                # print('not feasible')
                costs.append(500)
        return np.sum(costs)

    def is_feasible_iter(self, m, n):
        is_feasible = True
        if m > dss.linecodes_count()-1:
            is_feasible = False
        if n > dss.linecodes_count()-1:
            is_feasible = False
        if m < 0:
            is_feasible = False
        if n < 0:
            is_feasible = False
        return is_feasible

    def is_feasible(self, lines):
        is_feasible = True
        for x in lines:
            if x > dss.linecodes_count():
                is_feasible = False
            if x <= 0:
                is_feasible = False
        return is_feasible

    def constraint_adjacent_cable(self, lines):
        cost_matrix = self.CostMatrix()
        La = lines[0:-1]
        Lb = lines[1:]
        N = len(La)
        costs = []
        # if self.is_feasible(
        for k in range(N):
            m = La[k] - 1
            n = Lb[k] - 1
            if self.is_feasible_iter(m, n):
                if n <= m:
                    costs.append(0)
                else:
                    # line position [0 to N]
                    costs.append(cost_matrix[La[k]-1, Lb[k]-1])
            else:  # not feasible
                costs.append(500)
        return np.sum(costs)

    def circuit_loss_cost(self, lines):
        if self.is_feasible(lines) == True:
            PlossBase = np.real(
                np.sum(sc.DefaultLineLossDF().loc[:, 'PowerLoss']))
            Ploss = np.real(np.sum(sc.get_lineloss(lines).loc[:, 'PowerLoss']))
            Costs = (Ploss/PlossBase)*500
        else:
            Costs = 500
        return Costs

    def __set_default_lineloss_df(self):
        # (get_lineloss) criar uma classe dss e usar herança futuramente para limpar esse código.
        self.__default_lineloss_df = self.get_lineloss(self.DefaulLines())
        return self

    def get_lineloss(self, lines):
        # criar uma classe dss e usar herança futuramente para limpar esse código.
        dss_model = circuit_model(lines)
        dss = run_dss_model(dss_model, self.DSS())
        df = get_line_df(self.DSS())
        return df
    # def __set_dss_model()

    def __set_start_dss(self):
        self.__start_dss = start_dss()
        return self

    def __set_cost_matrix(self):
        self.__cost_matrix = np.array([
            [0, 100, 200, 400, 500],
            [100, 0, 100, 200, 400],
            [200, 100, 0, 150, 300],
            [400, 200, 150, 0, 200],
            [500, 400, 300, 200, 0]])
        return self

    def __set_default_lines(self):
        self.__default_lines = [4, 4, 4, 4, 1, 3, 2, 1, 1, 2, 2, 1, 3, 1,
                                1, 3, 1, 3, 1, 3, 3, 1, 1, 1, 4, 4, 1, 1,
                                4, 3, 3, 3, 3, 3, 3, 3, 3]
        return self
