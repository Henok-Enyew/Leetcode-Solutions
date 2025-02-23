from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder.pop(0))
        if preorder:
            left_subtree_root = preorder[0]
            left_subtree_size = postorder.index(left_subtree_root) + 1
            root.left = self.constructFromPrePost(preorder[:left_subtree_size], postorder[:left_subtree_size])
            root.right = self.constructFromPrePost(preorder[left_subtree_size:], postorder[left_subtree_size:-1])
        return root
