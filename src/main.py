from src.config import Config
from src.solvers.solvers_manager import SolverManager
from src.sudoku import Sudoku
from src.sudokus_examples.sudokus_initialization import ed_33


def run():
    config = Config()
    solver = SolverManager.init_solver(solver_name=config.solver)
    sudoku = Sudoku()
    ed_33(sudoku)
    sudoku = solver.solve_sudoku(sudoku)
    print(sudoku.grid)



if __name__ == "__main__":
    run()
