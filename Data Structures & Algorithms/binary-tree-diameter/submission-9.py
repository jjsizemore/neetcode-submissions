# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Diameter = longest path between any two nodes
        # Longest path through a node is leftHeight + rightHeight
        # Use a helper function that finds the greatest height of a given subtree
        # Use the helper function at each node on left & right, adding 2 for the current node's links

        res = 0
        
        if not root:
            return 0

        # Returns max height at node, updates res
        def dfs(root):
            nonlocal res

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)

        return res

