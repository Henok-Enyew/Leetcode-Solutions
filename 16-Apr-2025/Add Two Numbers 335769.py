# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = ''
        st2 = ''
        cur1, cur2, = l1, l2
        while cur1 or cur2:
            if cur1:
                st1 = str(cur1.val) + st1
                cur1 = cur1.next
            if cur2:
                st2 = str(cur2.val) + st2
                cur2 = cur2.next
        num1 = int(st1)
        num2 = int(st2)
        sm = num1 + num2
        sm = str(sm)[::-1]
        head = ListNode(int(sm[0]))
        cur = head
        for i in range(1,len(sm)):
            new_node = ListNode(int(sm[i]))
            cur.next = new_node
            cur = cur.next
        return head
