from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # We will use two pointers to find the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second part of the list
        prev = None
        curr = slow.next
        slow.next = None  # Break the cycle of the reversed list
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        # Merge the two lists interchanging nodes
        # One from the original list, and one from the reversed list
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2  # now head1 refers to head2
            head2 = nextt  # and head2 refers to head1

        return head


def create_list_node(numbers: List[int]) -> ListNode:
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

head = create_list_node([1, 2, 3, 4])
output = list_node_to_list(sol.reorderList(head))
expected = [1, 4, 2, 3]

head = create_list_node([1, 2, 3, 4, 5])
output = list_node_to_list(sol.reorderList(head))
expected = [1, 5, 2, 4, 3]
