from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        paths_num = [[0] * n for _ in range(m)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def available_paths(i: int, j: int) -> int:
            if paths_num[i][j]:
                return paths_num[i][j]

            paths_num[i][j] = 1

            for di, dj in directions:
                i1, j1 = i + di, j + dj
                if 0 <= i1 < m and 0 <= j1 < n and grid[i][j] > grid[i1][j1]:
                    paths_num[i][j] += available_paths(i1, j1) % mod

            return paths_num[i][j]

        return sum(available_paths(i, j) for i in range(m) for j in range(n)) % mod


sol = Solution()
# sol.countPaths([[1, 1], [3, 4]])
sol.countPaths([[1], [2]])
