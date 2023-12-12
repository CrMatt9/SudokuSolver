from abc import ABC, abstractmethod

from src.sudoku import Sudoku


class Solver(ABC):
    def __init__(self, solver_name:str):
        self._name = solver_name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def solve_sudoku(self, sudoku:Sudoku) -> Sudoku:
        raise NotImplementedError("Please Implement this method")
