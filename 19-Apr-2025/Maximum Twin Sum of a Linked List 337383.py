# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mp = {}
        current = head
        index = 0
        while current:
            mp[index] = current.val
            current = current.next
            index += 1
        i = 0
        # store
        max_sm = float('-inf')

        while i <= (index)/2:
            sm = mp[i] + mp[index - i - 1]
            max_sm = max(max_sm, sm)
            i += 1
        return max_sm
