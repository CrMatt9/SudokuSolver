from copy import deepcopy

from src.solvers.base_solver import Solver
from src.sudoku import Sudoku


class BruteForceSolver(Solver):
    def __init__(self, solver_name: str):
        super().__init__(solver_name=solver_name)

    def solve_sudoku(self, sudoku: Sudoku) -> Sudoku:
        grid_open_possibilities = sudoku.grid_open_possibilities
        thread_iteration = 0
        while grid_open_possibilities:
            number_of_options_per_cell = {
                cell: len(grid_open_possibilities[cell])
                for cell in grid_open_possibilities.keys()
                if len(grid_open_possibilities[cell]) > 0
            }
            minimum_possibilities = number_of_options_per_cell[
                min(number_of_options_per_cell, key=number_of_options_per_cell.get)
            ]
            cells_to_prioritize = {
                cell
                for cell in number_of_options_per_cell.keys()
                if number_of_options_per_cell[cell] == minimum_possibilities
            }
            if minimum_possibilities == 1:
                for cell in cells_to_prioritize:
                    input_with_possible_solution = sudoku.add_number(
                        number=grid_open_possibilities[cell].pop(),
                        row=cell.row,
                        column=cell.column,
                    )
                    if not input_with_possible_solution:
                        return sudoku

            else:
                cell_to_fill = sorted(cells_to_prioritize)[0]
                if thread_iteration >= len(grid_open_possibilities[cell_to_fill]):
                    return sudoku
                possibility_to_explore = sorted(grid_open_possibilities[cell_to_fill])[
                    thread_iteration
                ]
                sudoku_to_explore_solutions = deepcopy(sudoku)
                sudoku_to_explore_solutions.add_number(
                    number=possibility_to_explore,
                    row=cell_to_fill.row,
                    column=cell_to_fill.column,
                )
                sudoku_to_explore_solutions = self.solve_sudoku(sudoku_to_explore_solutions)
                if sudoku_to_explore_solutions.is_solved:
                    return sudoku_to_explore_solutions
                thread_iteration += 1

            grid_open_possibilities = sudoku.grid_open_possibilities

        return sudoku
