# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current and current.next:
            current = current.next
            count += 1
        count += 1
        mod = k % count
        index = count - mod
        print(index)
        i = 0
        last = current
        current = head
        while current and current.next:
            if i+1 == index:
                prev = current
                last.next = head
                head = current.next
                prev.next = None
                break
            else:
                current = current.next
            i += 1
        return head