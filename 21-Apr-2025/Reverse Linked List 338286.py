# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current = head
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        return prev_node