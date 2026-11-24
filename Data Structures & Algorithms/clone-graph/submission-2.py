"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS iterative soln with explicit stack

        if not node:
            return None

        toNew = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            stack = []

            stack.append(node)

            # create clone, add it to map
            # iterate through orig. neighbors, add neighbor clones via map
            # add neighbors to stack
            while stack:
                cur = stack.pop()

                if cur not in toNew:
                    toNew[cur] = Node(cur.val)

                for neighbor in cur.neighbors:
                    if neighbor not in toNew:
                        toNew[neighbor] = Node(neighbor.val)
                        stack.append(neighbor)

                    toNew[cur].neighbors.append(toNew[neighbor])

        dfs(node)
        
        return toNew[node]

        # Time  O(V + E)
        #   O(V) - each node is visited and copied once
        #   O(2E) -> O(E) - undirected edges show up twice, once in each endpoint's neighbor list
        # Space O(V) 
        #   O(V) auxiliary for toNew
        #   O(V) auxiliary for stack
        #   O(V + E) for output
            