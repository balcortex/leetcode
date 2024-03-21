from typing import List


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:

        dummy = list1  # save the location of the first node
        idx = 0

        # loop through all items to know the location of the items to remove
        while list1:
            if idx == a - 1:
                start = list1  # pointer to the previous node of deletion
            if idx == b:
                end = list1.next  # pointer to the next node of deletion
            idx += 1
            list1 = list1.next

        # Point the last item before index `a` to the start of list2
        start.next = list2

        # Get the location of the last item of list2
        while list2.next:
            list2 = list2.next

        # Point the last item of two to the end (the node after the deleted
        # ones) of list1
        list2.next = end

        # We stored the head of list1 in the dummy variable
        return dummy


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
list1 = createListNode([10, 1, 13, 6, 9, 5])
list2 = createListNode([1000000, 1000001, 1000002])
a = 3
b = 4
output = list_node_to_list(sol.mergeInBetween(list1, a, b, list2))
expected = [10, 1, 13, 1000000, 1000001, 1000002, 5]
assert output == expected
