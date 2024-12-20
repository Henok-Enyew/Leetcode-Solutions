class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left: TreeNode, right: TreeNode, level: int):
            if not left or not right:
                return
            
            if level % 2 == 1:
                left.val, right.val = right.val, left.val
            
            # Recursively process the next level
            dfs(left.left, right.right, level + 1)
            dfs(left.right, right.left, level + 1)
        
        # Start DFS with the root's children at level 1
        if root:
            dfs(root.left, root.right, 1)
        return root
