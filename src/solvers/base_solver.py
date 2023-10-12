from abc import ABC


class Solver(ABC):
    def __init__(self, solver_name:str):
        self._name = solver_name

    @property
    def name(self):
        return self._name

    def solve_sudoku(self, sudoku_matrix:Sudoku) -> Sudoku: