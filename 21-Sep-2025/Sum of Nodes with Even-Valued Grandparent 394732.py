# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(u, parent, grandParent):
            nonlocal ans
            if not u:
                return
            if grandParent is not None and grandParent % 2 == 0:
                ans += u.val
            dfs(u.left, u.val, parent)
            dfs(u.right, u.val, parent)
        ans = 0
        dfs(root, None, None)
        return ans
        