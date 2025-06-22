# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = len(nums)
        dummy = TreeNode()
        def helper(head, low, up):
            if low > up:
                return
            mid = (low + up) // 2
            hd = TreeNode(nums[mid])
            if low == 0 and up == len(nums) - 1:
                head.right = hd
            hd.left = helper(hd,low, mid-1)
            hd.right = helper(hd, mid+1,up)
            return hd
        helper(dummy, 0, l-1)
        return dummy.right
