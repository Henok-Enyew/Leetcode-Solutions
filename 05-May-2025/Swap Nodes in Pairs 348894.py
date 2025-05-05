# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        # prev = None
        new_head = ListNode(0)
        prev = new_head
        if current and not current.next:
            new_head.next = current
        # else:
        #     new_head.next = current
        while current and current.next:
            """ 
                node1.next = node2.next
                node2.next = node1
                node0.next = node2
            """
            prev.next = current.next
            current.next = current.next.next
            prev.next.next = current
            prev = current
            current = current.next
        return new_head.next


