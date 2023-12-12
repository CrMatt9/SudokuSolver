from src.solvers.base_solver import Solver
from src.solvers.brute_force import BruteForceSolver


class SolverManager:
    _implemented_solvers = {"brute_force": BruteForceSolver}

    @staticmethod
    def init_solver(solver_name: str) -> Solver:
        try:
            return SolverManager._implemented_solvers[solver_name](solver_name=solver_name)
        except KeyError:
            NotImplemented(
                f"The solver: {solver_name} has not been implemented, please select one of the already "
                f"implemented solvers: \n"
                f" {list(SolverManager._implemented_solvers.keys())}"
            )
