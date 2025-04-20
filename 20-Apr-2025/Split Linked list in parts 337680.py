# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        part = count // k
        extra = count % k

        current = head
        ans = []
        for _ in range(k):
            part_head = current
            size = part + (1 if extra > 0 else 0)
            extra -= 1

            for i in range(size - 1):
                if current:
                    current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part

            ans.append(part_head)
        
        return ans
