# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildMaxTree(self, nums, start, end):
        if start > end:
            return None
        mx = float('-inf')
        index = 0
        for i in range(start,end + 1):
            if nums[i] > mx:
                mx = nums[i]
                index = i
        root = TreeNode(mx)

        root.left = self.buildMaxTree(nums,start, index-1)
        root.right = self.buildMaxTree(nums, index+1, end)
        return root
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == None:
            return None
        return self.buildMaxTree(nums, 0, len(nums)-1)