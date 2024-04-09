from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # We'll make use of a counter to keep track the tickets bought
        time = 0

        # We need to run the cycle until we get a result
        while True:
            # Go trough the entire row each time
            for idx, ticket in enumerate(tickets):
                # If the person needs a ticket, increment the counter
                time += ticket > 0
                # We don't care about negative numbers
                tickets[idx] -= 1

                # If the person we are looking for have bought all their
                # tickets, return the number of tickets bought until now
                if tickets[k] == 0:
                    return time


sol = Solution()

tickets = [2, 3, 2]
k = 2
assert sol.timeRequiredToBuy(tickets, k) == 6

tickets = [5, 1, 1, 1]
k = 0
assert sol.timeRequiredToBuy(tickets, k) == 8
