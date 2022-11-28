from .subrectangle_queries import SubrectangleQueries


def test_base():
    rect = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    assert rect.getValue(0, 2) == 1
    rect.updateSubrectangle(0, 0, 3, 2, 5)
    assert rect.getValue(0, 2) == 5
    assert rect.getValue(3, 1) == 5
    rect.updateSubrectangle(3, 0, 3, 2, 10)
    assert rect.getValue(0, 2) == 5
    assert rect.getValue(3, 1) == 10


def test_base2():
    rect = SubrectangleQueries([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    assert rect.getValue(0, 0) == 1
    rect.updateSubrectangle(0, 0, 2, 2, 100)
    assert rect.getValue(0, 0) == 100
    assert rect.getValue(2, 2) == 100
    rect.updateSubrectangle(1, 1, 2, 2, 20)
    assert rect.getValue(2, 2) == 20
