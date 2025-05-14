# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        current  = root
        parent = current
        while current:
            parent = current
            if val >= current.val:
                current = current.right
            else:
                current = current.left
        if val >= parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root
        