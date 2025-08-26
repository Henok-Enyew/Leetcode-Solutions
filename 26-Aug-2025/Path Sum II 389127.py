# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(rt, arr):
            arr.append(rt.val)
            if not rt.left and not rt.right:
                if sum(arr) == targetSum:
                    res.append(arr.copy())
                    return
            if rt.right:
                dfs(rt.right, arr)
                arr.pop()
                 
            if rt.left:
                dfs(rt.left, arr)
                arr.pop()

        dfs(root, [])
        return res