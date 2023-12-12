from collections import namedtuple
from copy import copy
from itertools import product

from src.exceptions import InvalidInput
from src.solvers.resolution_log import ResolutionLog


class Sudoku:
    Coordinates = namedtuple("Coordinates", "row column")

    def __init__(self):
        self._row_structure = {i: set() for i in range(1, 10)}
        self._column_structure = {i: set() for i in range(1, 10)}
        self._squares_structure = {i: set() for i in range(1, 10)}
        self.grid = {
            self.Coordinates(row=i, column=j): None
            for i in range(1, 10)
            for j in range(1, 10)
        }

        self.grid_open_possibilities = {
            self.Coordinates(row=i, column=j): {_ for _ in range(1, 10)}
            for i in range(1, 10)
            for j in range(1, 10)
        }
        self.immutable_cells = set()
        self._resolution_log = ResolutionLog()

    @property
    def is_solved(self) -> bool:
        _is_solved = None not in self.grid.values()
        return _is_solved

    @property
    def resolution_log(self) -> ResolutionLog:
        return self._resolution_log


    @staticmethod
    def get_square(row: int, column: int) -> int:
        row_square_pos = Sudoku._get_square_position(cell_coordinate=row)
        column_square_pos = Sudoku._get_square_position(cell_coordinate=column)
        square = column_square_pos + 3 * (row_square_pos - 1)
        return square

    @staticmethod
    def _get_square_position(cell_coordinate: int) -> int:
        if cell_coordinate in {1, 2, 3}:
            return 1
        elif cell_coordinate in {4, 5, 6}:
            return 2
        else:
            return 3

    def is_valid_input(self, number: int, row: int, column: int) -> bool:
        if (
            self.is_immutable_cell(row=row, column=column)
            or not self.meets_row_rule(number=number, row=row)
            or not self.meets_column_rule(number=number, column=column)
            or not self.meets_square_rule(number=number, row=row, column=column)
        ):
            return False

        else:
            return True

    def meets_row_rule(
        self,
        number: int,
        row: int,
    ) -> bool:
        return number not in self._row_structure[row]

    def meets_column_rule(self, number: int, column: int) -> bool:
        return number not in self._column_structure[column]

    def meets_square_rule(self, number: int, row: int, column: int):
        square = self.get_square(row=row, column=column)
        return number not in self._squares_structure[square]

    def is_immutable_cell(self, row: int, column: int):
        return self.Coordinates(row=row, column=column) in self.immutable_cells

    def add_immutable_cell(self, number: int, row: int, column: int):
        self.add_number(number=number, row=row, column=column)
        self.immutable_cells.add(self.Coordinates(row=row, column=column))

    def add_number(self, number: int, row: int, column: int) -> bool:
        if self.is_valid_input(number=number, row=row, column=column):
            _square = self.get_square(row, column)
            cell = self.Coordinates(row=row, column=column)
            self.grid[cell] = number
            self._row_structure[row].add(number)
            self._column_structure[column].add(number)
            self._squares_structure[_square].add(number)
            assert len(self._row_structure[row]) <= 9
            assert len(self._row_structure[column]) <= 9
            assert len(self._squares_structure[_square]) <= 9
            self._resolution_log.add_step(sudoku=self, cell=cell, choice=number)
            input_with_possible_solution = self.update_grid_open_possibilities(
                cell_filled=cell
            )
            return input_with_possible_solution

        else:
            raise InvalidInput(
                f"The number {number} introduced in row {row} and column {column} is not valid"
            )

    def update_grid_open_possibilities(self, cell_filled=None):
        if cell_filled:
            del self.grid_open_possibilities[cell_filled]
        for row, column in product(range(1, 10), range(1, 10)):
            cell = self.Coordinates(row=row, column=column)
            if cell in self.grid_open_possibilities:
                _iterable = copy(self.grid_open_possibilities[cell])
                for possible_number in _iterable:
                    if not self.is_valid_input(
                        number=possible_number, row=row, column=column
                    ):
                        self.grid_open_possibilities[cell].remove(possible_number)
                if not self.grid_open_possibilities[cell]:
                    return False
        return True
