# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        left = None
        right = head
        while right:
            if n==0:
                left = head
            if n < 0:
                left = left.next
            right = right.next
            n -= 1
        if left == None:
            head = head.next
        else:
            left.next = left.next.next
        return head