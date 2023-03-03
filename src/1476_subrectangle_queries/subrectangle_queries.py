from typing_extensions import Self


class SubrectangleQueries:
    def __init__(self: Self, rectangle: list[list[int]]) -> None:
        self.rect = rectangle

    def updateSubrectangle(self: Self,  # noqa: N802
                           row1: int,
                           col1: int,
                           row2: int,
                           col2: int,
                           new_value: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rect[i][j] = new_value

    def getValue(self: Self, row: int, col: int) -> int:  # noqa: N802
        return self.rect[row][col]
