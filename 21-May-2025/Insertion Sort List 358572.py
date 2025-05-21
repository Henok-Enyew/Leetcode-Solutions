# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = head
        while current:
            next_node = current.next
            cur = dummy
            while cur.next and cur.next.val < current.val:
                cur = cur.next
            current.next = cur.next
            cur.next= current
            current = next_node
        return dummy.next