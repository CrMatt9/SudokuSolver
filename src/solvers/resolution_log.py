from collections import namedtuple
from copy import deepcopy


class ResolutionLog:
    Choice = namedtuple("Choice", "cell choice")

    def __init__(self):
        self.sudoku_log = {}
        self.possibilities_log = {}

    def add_step(self, sudoku, cell, choice):
        if not self.sudoku_log:
            step = 0
        else:
            step = max(self.sudoku_log.keys()) + 1

        self.sudoku_log[step] = deepcopy(sudoku.grid)
        self.possibilities_log[step] = self.Choice(cell=cell, choice=choice)
