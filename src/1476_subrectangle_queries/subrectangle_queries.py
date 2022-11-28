class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, new_value: int) -> None:  # noqa: N802
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rect[i][j] = new_value

    def getValue(self, row: int, col: int) -> int:  # noqa: N802
        return self.rect[row][col]
