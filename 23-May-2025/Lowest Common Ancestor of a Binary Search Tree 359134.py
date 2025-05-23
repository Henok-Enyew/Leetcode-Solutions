# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_list = []
        q_list = []
        def searchBSTP(rt):
            p_list.append(TreeNode(rt.val))
            if not rt:
                return None
            if p.val > rt.val:
                return searchBSTP(rt.right)
            elif p.val < rt.val:
                return searchBSTP(rt.left)
            else:
                return rt
        def searchBSTQ(rt):
            q_list.append(TreeNode(rt.val))
            if not rt:
                return None
            if q.val > rt.val:
                return searchBSTQ(rt.right)
            elif q.val < rt.val:
                return searchBSTQ(rt.left)
            else:
                return rt
        searchBSTP(root)
        searchBSTQ(root)
        lookup = {}
        for i in range(len(p_list)):
            lookup[p_list[i].val] = p_list[i] 
        for j in range(len(q_list)-1,-1,-1):
            if q_list[j].val in lookup:
                return q_list[j]