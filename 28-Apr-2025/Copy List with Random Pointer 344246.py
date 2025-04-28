# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        store = {}  # maps original node -> copied node

        # First pass: Create a copy of each node and store it in the map
        current = head
        while current:
            store[current] = Node(current.val)
            current = current.next

        # Second pass: Assign next and random pointers
        current = head
        while current:
            if current.next:
                store[current].next = store.get(current.next)
            if current.random:
                store[current].random = store.get(current.random)
            current = current.next

        return store[head]
