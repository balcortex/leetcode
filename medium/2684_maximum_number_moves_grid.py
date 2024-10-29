from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(row, col):
            # Last column, no more possible moves
            if col == n - 1:
                return 0

            # If we already visited this cell, return its memo value
            if memo[row][col] != -1:
                return memo[row][col]

            # If the cell is new, calculate the maximum number of moves
            # from that cell onwards
            max_moves = 0
            for dir_row, dir_col in ((-1, 1), (0, 1), (1, 1)):
                new_row, new_col = row + dir_row, col + dir_col

                # Check if the new cell is strictly greater than current cell
                # and if the values for the new row and new columns are in bounds
                if (
                    0 <= new_row < m
                    and new_col < n
                    and grid[new_row][new_col] > grid[row][col]
                ):
                    # If we can make a move, calculate recursively for the next cell
                    # (the +1 count the move of the current cell to the next)
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))

            # Store the maximum number of moves for this cell
            memo[row][col] = max_moves
            return max_moves

        # Calculate the maximum number of moves starting in the cells
        # on the first column
        moves = 0
        for row in range(m):
            moves = max(moves, dfs(row, 0))

        return moves


sol = Solution()

grid = [
    [2, 4, 3, 5],
    [5, 4, 9, 3],
    [3, 4, 2, 11],
    [10, 9, 13, 15],
]
expected = 3
assert sol.maxMoves(grid) == expected

grid = [
    [
        [3, 2, 4],
        [2, 1, 9],
        [1, 1, 7],
    ]
]
expected = 0
assert sol.maxMoves(grid) == expected
