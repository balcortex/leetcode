from typing import List


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # We need to pointers, fast will travel at double the speed of slow
        # When fast reaches the end, slow will be at the middle
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Reverse the second half of the list (from middle to end)
        prev, slow = slow, slow.next
        prev.next = None  # Break the reverse cycle
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # Compare the two halves of the list
        fast = head  # fast starts at the beginning
        slow = prev  # slow starts at the end
        while slow:  # stop the cycle at the middle (we broke the reverse cycle)
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True


def createListNode(numbers: List[int]) -> ListNode:
    cur = dummy = ListNode(0)
    for num in numbers:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def list_node_to_list(list_node: ListNode) -> List[int]:
    lst = []
    while list_node:
        lst.append(list_node.val)
        list_node = list_node.next
    return lst


sol = Solution()
expected = True
output = sol.isPalindrome(createListNode([1, 2, 2, 1]))
assert output == expected

expected = False
output = sol.isPalindrome(createListNode([1, 2]))
assert output == expected
