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


        # returns the max height at a given node & updates isBalanced if
        # the node's left and right subtrees differ in height by more than 1
        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
        
            return max(left, right) + 1
            
        return dfs(root) != -1