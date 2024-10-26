# The celebrity problem
# https://www.geeksforgeeks.org/the-celebrity-problem/

from typing import List


def celebrity(people: List[List[int]], n: int):
    # Balance between how many people the person[i] knows
    # and how many people known the person[i]
    known = [0] * n

    # For every person j
    for j, person in enumerate(people):
        # For every person[i] that is known by person[j]
        for i, knows in enumerate(person):
            # If person[j] knows someone, decrease its value
            known[j] -= knows == 1
            # If person[i] is known by person[j], increase its value
            known[i] += knows == 1

    # Traverse the known list
    for i, k in enumerate(known):
        # Only the person who is known by everybody, but knows no one
        # is the superstar, so its `known` balance must be (n - 1)
        if k == n - 1:
            return i

    return -1


people = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
n = 4

assert celebrity(people, n) == 2

people = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
n = 4

assert celebrity(people, n) == -1
