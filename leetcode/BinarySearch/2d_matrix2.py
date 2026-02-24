class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                l = mid + 1
        return False
