from collections import namedtuple


class Sudoku:
    Coordinates = namedtuple("Coordinates", "row column")

    def __init__(self):
        self._row_structure = {i: [None for _ in range(9)] for i in range(9)}
        self._column_structure = {i: [None for _ in range(9)] for i in range(9)}
        self._squares_structure = {i: [None for _ in range(9)] for i in range(9)}
        self.grid = {
            self.Coordinates(row=i, column=j): None for i in range(9) for j in range(9)
        }

    def _add_number(self, number: int, row: int, column: int):
        self.grid[self.Coordinates(row=row, column=column)] = number

    def _remove_number(self, number: int, row: int, column: int):
        self.grid[self.Coordinates(row=row, column=column)] = number