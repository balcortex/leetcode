from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Go trough all sandwiches
        while sandwiches:
            # If the first sandwich is wanted by some student
            # Remove both the sandwich and the student
            if sandwiches[0] in students:
                students.remove(sandwiches[0])
                sandwiches.pop(0)
            # If no one wants the first sandwich, end the cycle
            else:
                break
        # Return the number of students left (unable to eat)
        return len(students)


sol = Solution()

students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
assert sol.countStudents(students, sandwiches) == 0

students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
assert sol.countStudents(students, sandwiches) == 3
