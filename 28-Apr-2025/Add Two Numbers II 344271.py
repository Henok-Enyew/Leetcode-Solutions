# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        num1 = ''
        num2 = ''
        while current:
            num1 += str(current.val)
            current =current.next
        current = l2    
        while current:
            num2 += str(current.val)
            current =current.next
        sm = int(num1) + int(num2)
        sm = str(sm)
        dummy = ListNode(0)
        current = dummy
        for s in sm:
            new = ListNode(int(s))
            current.next =new
            current = new
        return dummy.next