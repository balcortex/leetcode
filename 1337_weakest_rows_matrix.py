from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ones_per_row = {index: sum(row) for index, row in enumerate(mat)}
        return sorted(ones_per_row, key=ones_per_row.get)[:k]


sol = Solution()

sol.kWeakestRows(
    mat=[
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ],
    k=3,
)
