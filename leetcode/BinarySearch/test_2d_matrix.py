import pytest


class Solution:
    # first we have to identify middle row, we should take it range minimal,
    # maximum and check if our target in range, than we perform Binary Search inside this row
    # if target smaller than minimal (matrix[i][0]) than we should continue processing only the remaining left matrixes
    # if target bigger than maximum (matrix[i][-1]) than continue processing right matrixes
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def _searchMatrixRows(min: int, max: int) -> int | None:
            middle = min + (max - min) // 2

            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                return middle
            if max - min <= 1:
                return None
            elif target < matrix[middle][0]:
                matrixIdx = _searchMatrixRows(min, middle)
            else:
                matrixIdx = _searchMatrixRows(middle, max)
            return matrixIdx

        def _searchMatrixElements(matrix_idx: int, l: int, r: int):
            middle = l + (r - l) // 2
            if target == matrix[matrix_idx][middle]:
                return True
            if r - l <= 1:
                return False
            elif target < matrix[matrix_idx][middle]:
                return _searchMatrixElements(matrix_idx, l, middle)
            else:
                return _searchMatrixElements(matrix_idx, middle, r)

        matrixRow = _searchMatrixRows(0, len(matrix))

        if matrixRow is None:
            return False
        return _searchMatrixElements(matrixRow, 0, len(matrix[matrixRow]))


@pytest.fixture
def s():
    return Solution()


def test_basic_true(s):
    assert s.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10)


def test_basic_false(s):
    assert not s.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15)
