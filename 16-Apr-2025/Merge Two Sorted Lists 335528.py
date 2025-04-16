# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        head = list1 if list1.val <= list2.val else list2
        new = head
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            next_node = None
            if cur1.val <= cur2.val:
                next_node = cur1
                cur1 = cur1.next
            else:
                next_node = cur2
                cur2 = cur2.next
            new.next = next_node
            new = new.next
        if cur1:
            new.next = cur1
        if cur2:
            new.next = cur2
        return head
        