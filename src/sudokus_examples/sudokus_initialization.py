def init_beginner_sudoku(sudoku):
    sudoku.add_immutable_cell(number=3, row=1, column=3)
    sudoku.add_immutable_cell(number=2, row=1, column=7)
    sudoku.add_immutable_cell(number=6, row=2, column=2)
    sudoku.add_immutable_cell(number=9, row=2, column=4)
    sudoku.add_immutable_cell(number=8, row=2, column=5)
    sudoku.add_immutable_cell(number=4, row=2, column=8)
    sudoku.add_immutable_cell(number=3, row=2, column=9)
    sudoku.add_immutable_cell(number=4, row=3, column=1)
    sudoku.add_immutable_cell(number=9, row=3, column=2)
    sudoku.add_immutable_cell(number=3, row=3, column=5)
    sudoku.add_immutable_cell(number=1, row=3, column=6)
    sudoku.add_immutable_cell(number=6, row=3, column=9)
    sudoku.add_immutable_cell(number=9, row=4, column=1)
    sudoku.add_immutable_cell(number=7, row=4, column=3)
    sudoku.add_immutable_cell(number=8, row=4, column=7)
    sudoku.add_immutable_cell(number=6, row=4, column=8)
    sudoku.add_immutable_cell(number=4, row=5, column=2)
    sudoku.add_immutable_cell(number=9, row=5, column=5)
    sudoku.add_immutable_cell(number=8, row=5, column=6)
    sudoku.add_immutable_cell(number=5, row=6, column=3)
    sudoku.add_immutable_cell(number=4, row=6, column=4)
    sudoku.add_immutable_cell(number=7, row=6, column=6)
    sudoku.add_immutable_cell(number=1, row=6, column=7)
    sudoku.add_immutable_cell(number=9, row=6, column=9)
    sudoku.add_immutable_cell(number=6, row=7, column=1)
    sudoku.add_immutable_cell(number=3, row=7, column=6)
    sudoku.add_immutable_cell(number=9, row=7, column=7)
    sudoku.add_immutable_cell(number=5, row=7, column=9)
    sudoku.add_immutable_cell(number=5, row=8, column=1)
    sudoku.add_immutable_cell(number=8, row=8, column=3)
    sudoku.add_immutable_cell(number=1, row=8, column=4)
    sudoku.add_immutable_cell(number=7, row=8, column=8)
    sudoku.add_immutable_cell(number=2, row=8, column=9)
    sudoku.add_immutable_cell(number=2, row=9, column=1)
    sudoku.add_immutable_cell(number=9, row=9, column=3)
    sudoku.add_immutable_cell(number=5, row=9, column=5)
    sudoku.add_immutable_cell(number=6, row=9, column=6)
    sudoku.add_immutable_cell(number=3, row=9, column=8)
    sudoku.add_immutable_cell(number=8, row=9, column=9)


def init_intermediate_sudoku(sudoku):
    sudoku.add_immutable_cell(number=2, row=1, column=2)
    sudoku.add_immutable_cell(number=4, row=1, column=3)
    sudoku.add_immutable_cell(number=3, row=1, column=4)
    sudoku.add_immutable_cell(number=8, row=1, column=5)
    sudoku.add_immutable_cell(number=6, row=2, column=6)
    sudoku.add_immutable_cell(number=7, row=2, column=9)
    sudoku.add_immutable_cell(number=5, row=3, column=2)
    sudoku.add_immutable_cell(number=8, row=3, column=3)
    sudoku.add_immutable_cell(number=4, row=3, column=7)
    sudoku.add_immutable_cell(number=4, row=4, column=1)
    sudoku.add_immutable_cell(number=1, row=4, column=5)
    sudoku.add_immutable_cell(number=7, row=5, column=4)
    sudoku.add_immutable_cell(number=5, row=5, column=6)
    sudoku.add_immutable_cell(number=2, row=6, column=5)
    sudoku.add_immutable_cell(number=8, row=6, column=9)
    sudoku.add_immutable_cell(number=1, row=7, column=3)
    sudoku.add_immutable_cell(number=6, row=7, column=7)
    sudoku.add_immutable_cell(number=7, row=7, column=8)
    sudoku.add_immutable_cell(number=3, row=8, column=1)
    sudoku.add_immutable_cell(number=5, row=8, column=4)
    sudoku.add_immutable_cell(number=4, row=9, column=5)
    sudoku.add_immutable_cell(number=9, row=9, column=6)
    sudoku.add_immutable_cell(number=2, row=9, column=7)
    sudoku.add_immutable_cell(number=1, row=9, column=8)


def init_difficult_sudoku(sudoku):
    sudoku.add_immutable_cell(number=1, row=1, column=2)
    sudoku.add_immutable_cell(number=8, row=1, column=6)
    sudoku.add_immutable_cell(number=5, row=1, column=8)
    sudoku.add_immutable_cell(number=6, row=2, column=3)
    sudoku.add_immutable_cell(number=9, row=2, column=7)
    sudoku.add_immutable_cell(number=3, row=2, column=9)
    sudoku.add_immutable_cell(number=2, row=3, column=1)
    sudoku.add_immutable_cell(number=3, row=3, column=3)
    sudoku.add_immutable_cell(number=5, row=3, column=4)
    sudoku.add_immutable_cell(number=9, row=3, column=5)
    sudoku.add_immutable_cell(number=4, row=3, column=9)
    sudoku.add_immutable_cell(number=8, row=4, column=1)
    sudoku.add_immutable_cell(number=4, row=4, column=4)
    sudoku.add_immutable_cell(number=7, row=4, column=6)
    sudoku.add_immutable_cell(number=2, row=5, column=3)
    sudoku.add_immutable_cell(number=3, row=5, column=7)
    sudoku.add_immutable_cell(number=2, row=6, column=4)
    sudoku.add_immutable_cell(number=5, row=6, column=6)
    sudoku.add_immutable_cell(number=1, row=6, column=9)
    sudoku.add_immutable_cell(number=9, row=7, column=1)
    sudoku.add_immutable_cell(number=5, row=7, column=5)
    sudoku.add_immutable_cell(number=2, row=7, column=6)
    sudoku.add_immutable_cell(number=4, row=7, column=7)
    sudoku.add_immutable_cell(number=8, row=7, column=9)
    sudoku.add_immutable_cell(number=1, row=8, column=1)
    sudoku.add_immutable_cell(number=8, row=8, column=3)
    sudoku.add_immutable_cell(number=5, row=8, column=7)
    sudoku.add_immutable_cell(number=2, row=9, column=2)
    sudoku.add_immutable_cell(number=9, row=9, column=4)
    sudoku.add_immutable_cell(number=1, row=9, column=8)


def ed_33(sudoku):
    sudoku.add_immutable_cell(number=5, row=1, column=3)
    sudoku.add_immutable_cell(number=2, row=1, column=5)
    sudoku.add_immutable_cell(number=4, row=2, column=1)
    sudoku.add_immutable_cell(number=9, row=2, column=9)
    sudoku.add_immutable_cell(number=9, row=3, column=3)
    sudoku.add_immutable_cell(number=6, row=3, column=4)
    sudoku.add_immutable_cell(number=7, row=3, column=5)
    sudoku.add_immutable_cell(number=5, row=3, column=7)
    sudoku.add_immutable_cell(number=7, row=4, column=2)
    sudoku.add_immutable_cell(number=6, row=4, column=3)
    sudoku.add_immutable_cell(number=2, row=4, column=9)
    sudoku.add_immutable_cell(number=5, row=5, column=2)
    sudoku.add_immutable_cell(number=1, row=5, column=8)
    sudoku.add_immutable_cell(number=3, row=6, column=1)
    sudoku.add_immutable_cell(number=4, row=6, column=7)
    sudoku.add_immutable_cell(number=8, row=6, column=8)
    sudoku.add_immutable_cell(number=2, row=7, column=3)
    sudoku.add_immutable_cell(number=1, row=7, column=5)
    sudoku.add_immutable_cell(number=9, row=7, column=6)
    sudoku.add_immutable_cell(number=7, row=7, column=7)
    sudoku.add_immutable_cell(number=5, row=8, column=1)
    sudoku.add_immutable_cell(number=1, row=8, column=9)
    sudoku.add_immutable_cell(number=6, row=9, column=5)
    sudoku.add_immutable_cell(number=3, row=9, column=7)


def ed_34(sudoku):
    sudoku.add_immutable_cell(number=6, row=1, column=2)
    sudoku.add_immutable_cell(number=8, row=1, column=4)
    sudoku.add_immutable_cell(number=2, row=1, column=6)
    sudoku.add_immutable_cell(number=7, row=1, column=8)
    sudoku.add_immutable_cell(number=1, row=2, column=1)
    sudoku.add_immutable_cell(number=7, row=2, column=4)
    sudoku.add_immutable_cell(number=3, row=2, column=6)
    sudoku.add_immutable_cell(number=5, row=2, column=9)
    sudoku.add_immutable_cell(number=9, row=3, column=3)
    sudoku.add_immutable_cell(number=2, row=3, column=7)
    sudoku.add_immutable_cell(number=4, row=4, column=1)
    sudoku.add_immutable_cell(number=3, row=4, column=9)
    sudoku.add_immutable_cell(number=3, row=5, column=2)
    sudoku.add_immutable_cell(number=5, row=5, column=8)
    sudoku.add_immutable_cell(number=8, row=6, column=3)
    sudoku.add_immutable_cell(number=1, row=6, column=4)
    sudoku.add_immutable_cell(number=9, row=6, column=6)
    sudoku.add_immutable_cell(number=6, row=6, column=7)
    sudoku.add_immutable_cell(number=7, row=8, column=1)
    sudoku.add_immutable_cell(number=4, row=8, column=4)
    sudoku.add_immutable_cell(number=8, row=8, column=6)
    sudoku.add_immutable_cell(number=1, row=8, column=9)
    sudoku.add_immutable_cell(number=3, row=9, column=3)
    sudoku.add_immutable_cell(number=5, row=9, column=7)
