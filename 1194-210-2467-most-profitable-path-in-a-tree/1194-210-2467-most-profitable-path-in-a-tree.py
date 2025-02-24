from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Step 1: Construct the tree as an adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Find Bob's path to root and store the time he reaches each node
        bob_path = {}
        path = []
        
        def find_bob_path(node, parent):
            if node == bob:
                path.append(node)
                for i, n in enumerate(reversed(path)):
                    bob_path[n] = i
                return True
            path.append(node)
            for neighbor in tree[node]:
                if neighbor != parent and find_bob_path(neighbor, node):
                    return True
            path.pop()
            return False
        
        find_bob_path(0, -1)
        
        # Step 3: DFS for Alice to maximize profit
        max_profit = float('-inf')
        
        def dfs(node, parent, depth, current_profit):
            nonlocal max_profit
            
            # Step 3.1: Compute Alice's profit at the current node
            if node in bob_path:
                if depth < bob_path[node]:
                    current_profit += amount[node]  # Alice reaches first
                elif depth == bob_path[node]:
                    current_profit += amount[node] // 2  # They reach together
            else:
                current_profit += amount[node]
            
            # Step 3.2: Check if it's a leaf node
            is_leaf = True
            for neighbor in tree[node]:
                if neighbor != parent:
                    is_leaf = False
                    dfs(neighbor, node, depth + 1, current_profit)
            
            if is_leaf:
                max_profit = max(max_profit, current_profit)
        
        dfs(0, -1, 0, 0)
        
        return max_profit
