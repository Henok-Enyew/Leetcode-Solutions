# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.space = k
        self.left = Node(0)  # Sentinel node
        self.right = Node(0)  # Sentinel node
        self.left.next = self.right
        self.right.prev = self.left

    def insertFront(self, value: int) -> bool:
        if self.space <= 0:
            return False
        new = Node(value, self.left.next, self.left)
        self.left.next.prev = new
        self.left.next = new
        self.space -= 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.space <= 0:
            return False
        new = Node(value, self.right, self.right.prev)
        self.right.prev.next = new
        self.right.prev = new
        self.space -= 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        to_delete = self.left.next
        self.left.next = to_delete.next
        to_delete.next.prev = self.left
        self.space += 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        to_delete = self.right.prev
        self.right.prev = to_delete.prev
        to_delete.prev.next = self.right
        self.space += 1
        return True

    def getFront(self) -> int:
        return self.left.next.val if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.right.prev.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0
