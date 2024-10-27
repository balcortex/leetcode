from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [
            [0] * len(row) for row in matrix
        ]  # Create a dp table with the same dimensions as matrix.
        count = 0  # Initialize count of square submatrices.

        for row in range(len(matrix)):  # Iterate through each row.
            for col in range(len(matrix[0])):  # Iterate through each column.
                if (
                    matrix[row][col] == 1
                ):  # Only proceed if the current cell in matrix is 1.
                    if (
                        row == 0 or col == 0
                    ):  # For the first row or first column, the largest square is just itself.
                        dp[row][col] = 1
                    else:
                        # Get the values of adjacent cells (up-left, left, up).
                        up_left = dp[row - 1][col - 1]
                        left = dp[row][col - 1]
                        up = dp[row - 1][col]
                        # Find the minimum of the three and add 1.
                        dp[row][col] = min(up_left, left, up) + 1

                # Add the value of dp[row][col] to the count.
                count += dp[row][col]

        return count  # Return the total count of square submatrices.


sol = Solution()

matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
expected = 15
assert sol.countSquares(matrix) == expected


matrix = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
expected = 7
assert sol.countSquares(matrix) == expected
