from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        # Dimensions of the grid
        # `j` refers to rows and `i` to columns
        n_rows = len(land)
        n_cols = len(land[0])

        # Here we store the limits of each group
        # [j_start, i_start, j_end, i_end]
        groups = []

        # Helper function to retrieve the bottom right corner of a group
        def find_coordinates(j: int, i: int) -> List[int]:
            # If the indices are out of boundaries, the adjacent cell forest (0),
            # or we already marked that cell (-1), return [-1, -1]
            # These negative indices doesn't affect the max function
            if i < 0 or j < 0 or i >= n_cols or j >= n_rows or land[j][i] != 1:
                return [-1, -1]

            # Mark the current cell as visited
            land[j][i] = -1

            # Visit the down and right neighbors to check if the group can
            # extend to this neighbors
            # Left and up neighbors are omitted because we are traversing the
            # original grid in this manner (they are visited anyways)
            j_down, i_down = find_coordinates(j + 1, i)
            j_right, i_right = find_coordinates(j, i + 1)

            # Find the maximum between the original cell and the two neighbors
            j_max = max(j, j_down, j_right)
            i_max = max(i, i_down, i_right)

            # Return the indices of the bottom right corner
            return [j_max, i_max]

        # Visit each cell in the grid
        for j, row in enumerate(land):
            for i, cell in enumerate(row):

                # If the cell doesn't contain a 1, go to the next cell
                if cell != 1:
                    continue

                # If we find a 1, find the bottom right corner (the upper left
                # corner is already in the variables j, i).
                j_end, i_end = find_coordinates(j, i)
                groups.append([j, i, j_end, i_end])

        return groups


sol = Solution()

land = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
expected = [[0, 0, 0, 0], [1, 1, 2, 2]]
assert sol.findFarmland(land) == expected

land = [[1, 1], [1, 1]]
expected = [[0, 0, 1, 1]]
assert sol.findFarmland(land) == expected

land = [[0]]
expected = []
assert sol.findFarmland(land) == expected
