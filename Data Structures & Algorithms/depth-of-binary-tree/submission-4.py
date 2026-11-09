# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        # Base case node is None, return 0
        # Return max of recursive call on children + 1

        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1