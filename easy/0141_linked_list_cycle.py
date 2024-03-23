from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use two pointers to detect the cycle
        # Fast has double the speed of slow
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If the two pointers meet, there is a loop
            if slow == fast:
                return True

        # If we reach the end, there is no loop
        return False


def listnode_from_list(lst: List[int], pos: int = -1) -> ListNode:
    # pos: the index of the node that is connected to the last node's next

    cur = dummy = ListNode(0)

    if pos < 0:
        pos = None

    for i, num in enumerate(lst):
        cur.next = ListNode(num)
        cur = cur.next
        if pos == i:
            temp = cur
    if pos is not None:
        cur.next = temp

    return dummy.next


sol = Solution()

head = listnode_from_list([3, 2, 0, 4], pos=1)
output = sol.hasCycle(head)
expected = True
assert output == expected

head = listnode_from_list([1, 2], pos=0)
output = sol.hasCycle(head)
expected = True
assert output == expected

head = listnode_from_list([1], pos=-1)
output = sol.hasCycle(head)
expected = False
assert output == expected

head = listnode_from_list([1, 2, 3, 4, 5], pos=-1)
output = sol.hasCycle(head)
expected = False
assert output == expected
