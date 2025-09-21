# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = set()

        def dfs(node: TreeNode, dist: int):
            if node == None:
                return

            if dist == k:
                res.add(node.val)
                return

            dfs(node.left, dist+1)
            dfs(node.right, dist+1)

        dfs(target, 0)

        def manipulate(node: TreeNode, parent: TreeNode):
            if node == None:
                return 0
            
            if node == target:
                node.left = parent
                node.right = None
                return -1
            
            if manipulate(node.left, node) == -1:
                node.left = parent
                return -1

            elif manipulate(node.right, node) == -1:
                node.right = parent
                return -1
            
            return 0
        
        manipulate(root, None)
        dfs(target, 0)

        return list(res)