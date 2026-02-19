from collections import defaultdict


# Difficulty: Medium (easy side)
# Self-solved: ~85-90%
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        sudoku_dict = defaultdict(set)
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                if board[row][col] == ".":
                    continue
                current_item = int(board[row][col])
                box_key = (row // 3, col // 3)
                if (
                    current_item in row_dict[row]
                    or current_item in column_dict[col]
                    or current_item in sudoku_dict[box_key]
                ):
                    return False
                row_dict[row].add(current_item)
                column_dict[col].add(current_item)
                sudoku_dict[box_key].add(current_item)

        return True
