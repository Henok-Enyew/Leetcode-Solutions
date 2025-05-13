# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_list = []

        def preorder(node):
            if not node:
                return
            preorder_list.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return preorder_list