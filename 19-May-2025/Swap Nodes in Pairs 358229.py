# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new_head = ListNode(0)
        prev = new_head
        if current and not current.next:
            new_head.next = current
        while current and current.next:
            prev.next = current.next
            current.next = current.next.next
        # dsfsd
            prev.next.next = current
            prev = current
            current = current.next
        return new_head.next


