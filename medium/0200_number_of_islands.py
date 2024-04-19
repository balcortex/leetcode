from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Dimensions of the grid
        # `j` refers to rows and `i` to columns
        n_rows = len(grid)
        n_cols = len(grid[0])

        # Here we store the number of islands
        count = 0

        # Auxiliary function to mark as `#` all the adjacent cells containing `1`
        def mark_neighbors(j: int, i: int) -> None:
            # If the indices are out of boundaries, the adjacent is water ('0'),
            # or we already marked that cell ('#'), exit the function
            if i < 0 or j < 0 or i >= n_cols or j >= n_rows or grid[j][i] != "1":
                return

            # Mark the current cell as visited
            grid[j][i] = "#"

            # Visit the neighbors and try to mark them
            for j_neigh, i_neigh in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                mark_neighbors(j + j_neigh, i + i_neigh)

        # Visit each cell in the grid
        for j, row in enumerate(grid):
            for i, cell in enumerate(row):

                # If the cell doesn't contain a "1", go to the next cell
                if cell != "1":
                    continue

                # If we find a "1", increase the counter, and mark the neighbors
                count += 1
                mark_neighbors(j, i)

        return count


sol = Solution()

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
assert sol.numIslands(grid) == 1

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
assert sol.numIslands(grid) == 3
