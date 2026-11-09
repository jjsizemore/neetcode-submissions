# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        # Use a stack, storing tuples of nodes and their depths

        if not root:
            return 0

        stack = [((root, 1))]

        maxDepth = 0

        while stack:
            cur, depth = stack.pop()

            if not cur:
                continue
            
            maxDepth = max(maxDepth, depth)

            stack.append((cur.left, depth + 1))
            stack.append((cur.right, depth + 1))

        return maxDepth
        