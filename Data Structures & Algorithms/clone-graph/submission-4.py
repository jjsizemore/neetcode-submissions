"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS Recursive Soln

        if not node:
            return

        toNew = {}
        
        def dfs(node):
            if node in toNew:
                return toNew[node]

            clone = Node(node.val)
            toNew[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return toNew[node]

        return dfs(node)

        # Time  O(V + E) - each node visited once and inner loop runs each way for each edge because the edges are undirected
        # Space O(V) - call stack
