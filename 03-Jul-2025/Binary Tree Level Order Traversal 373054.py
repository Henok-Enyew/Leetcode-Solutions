# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        levels = []
        queue = deque([(root,0)])
        curlevel = []
        #
        while queue:
            node,nodelevel = queue.popleft()
            if not node:
                continue

            if nodelevel != level:
                level += 1
                levels.append(curlevel[:])
                curlevel = []
            
            queue.append((node.left, nodelevel+1))
            queue.append((node.right, nodelevel+1))
            curlevel.append(node.val)
        if curlevel:
            levels.append(curlevel[:])
        return levels