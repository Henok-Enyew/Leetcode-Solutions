# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        while len(queue) > 0:
            prev = None
            for i in range(len(queue)):
                cur = queue.popleft()
                if prev and level %2 == 0 and prev.val >= cur.val:
                    return False
                if prev and level %2 != 0 and prev.val <= cur.val:
                    return False
                prev = cur
                if (level %2 == 0 and cur.val %2 == 0) or (cur.val %2 != 0 and level %2 != 0):
                    return False
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return True