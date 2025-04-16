# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mp = {}
        count = 0 
        current = head
        while current:
            mp[count] = current
            current = current.next
            count += 1
        mid = math.floor(count / 2) if count %2 == 1 else count / 2 
        return mp[mid]
        