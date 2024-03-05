from typing import List


class Solution1:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed = [list(row) for row in zip(*grid)]

        counter = 0

        for row in grid:
            for col in transposed:
                if row == col:
                    counter += 1

        return counter


# Best solution
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = {}

        for row in (tuple(row) for row in grid):
            dic[row] = dic.get(row, 0) + 1

        return sum(dic.get(col, 0) for col in zip(*grid))


class Solution2:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = {tuple(row): grid.count(row) for row in grid}
        return sum(dic.get(col, 0) for col in zip(*grid))


sol = Solution()
sol.equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]])
# sol.equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
# sol.equalPairs(grid=[[13, 13], [13, 13]])

# sol.equalPairs(
#     grid=[
#         [3, 3, 3, 6, 18, 3, 3, 3, 3, 3],
#         [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
#         [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
#         [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
#         [1, 1, 1, 11, 19, 1, 1, 1, 1, 1],
#         [3, 3, 3, 18, 19, 3, 3, 3, 3, 3],
#         [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
#         [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
#         [3, 3, 3, 1, 6, 3, 3, 3, 3, 3],
#         [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
#     ]
# )
