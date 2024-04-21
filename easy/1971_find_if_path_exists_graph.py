from typing import List
from collections import deque


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        # The deque and the set are more efficient than lists

        dic = {}  # store the source: [destinations] pairs
        stack = deque()  # keep track of the remaining destinations to visit
        visited = set()  # keep track of the visited destinations

        # Fill the dic using the source as the key, and the value are the
        # possible destinations to reach from that node (stored as a list,
        # because we can get to different destinations from the same source)
        for i, j in edges:
            dic.setdefault(i, []).append(j)
            dic.setdefault(j, []).append(i)  # both directions

        # Start visiting the source node
        stack.append(source)
        visited.add(source)

        # Try to reach the destination node, starting from source
        while stack:
            cur = stack.pop()  # current node
            if cur == destination:  # if we reach the destination, return True
                return True

            # Get all possible destinations from the current node
            for next_ in dic[cur]:
                # If we haven't visited this node yet, add it to the stack and
                # the visited set.
                if next_ not in visited:
                    stack.append(next_)
                    visited.add(next_)

        # If can't reach the destination, return False
        return False


sol = Solution()

n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
expected = True
assert sol.validPath(n, edges, source, destination) == expected

n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
expected = False
assert sol.validPath(n, edges, source, destination) == expected

n = 10
edges = [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]]
source = 7
destination = 5
expected = True
assert sol.validPath(n, edges, source, destination) == expected
