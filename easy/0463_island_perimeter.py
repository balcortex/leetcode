from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0  # Keep track of the sides touching water

        n_rows = len(grid)
        n_cols = len(grid[0])

        # Go through each cell
        for j, row in enumerate(grid):
            for i, cell in enumerate(row):
                # If the cell is water (i.e., 0), skip to the next cell
                if not cell:
                    continue

                # If we have land (i.e., 1), add the four sides to the perimeter
                perim += 4

                # Check the neighbors to remove shared sides
                # We need to ensure the limits of the indices
                # For example, cells in the first row don't have up neighbors
                if j > 0:
                    perim -= grid[j - 1][i]  # Up neighbors
                if i < n_cols - 1:
                    perim -= grid[j][i + 1]  # Right neighbors
                if j < n_rows - 1:
                    perim -= grid[j + 1][i]  # Down neighbors
                if i > 0:
                    perim -= grid[j][i - 1]  # Left neighbors

        return perim


sol = Solution()

grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
assert sol.islandPerimeter(grid) == 16

grid = [[1]]
assert sol.islandPerimeter(grid) == 4

grid = [[1, 1]]
assert sol.islandPerimeter(grid) == 6

grid = [[1, 0]]
assert sol.islandPerimeter(grid) == 4

grid = [[0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 0]]
assert sol.islandPerimeter(grid) == 18

grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
assert sol.islandPerimeter(grid) == 16

# It also works with islands

grid = [[0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 1]]
assert sol.islandPerimeter(grid) == 24
