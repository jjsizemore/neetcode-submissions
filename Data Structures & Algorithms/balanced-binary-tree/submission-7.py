# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Use a recursive dfs helper function to calculate the height of the tree
        # At each node we can compare the heights of the left and right subtrees


        # returns the max height at a given node, but returns -1 if a subtree is imbalanced
        # short circuits on receiving -1 for a subtree
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if (left == -1 or 
                right == -1 or
                abs(left - right) > 1):
                return -1

            return max(left, right) + 1
            
        return dfs(root) != -1