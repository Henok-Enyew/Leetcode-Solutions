# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        level = 0

        while queue:
            prev_val = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val))) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or (prev_val is not None and node.val >= prev_val))):
                    return False

                prev_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True