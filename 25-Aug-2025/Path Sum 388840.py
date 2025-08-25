# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(rt, sm):
            sm += rt.val
            if not rt.left and not rt.right :
                return sm == targetSum
            left_ok = dfs(rt.left, sm) if rt.left else False
            right_ok = dfs(rt.right, sm) if rt.right else False
            return left_ok or right_ok

        return dfs(root, 0)                