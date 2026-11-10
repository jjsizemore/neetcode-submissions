# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS with a helper function that takes a node and its upper and lower bounds
        def dfs(node, lower, upper) -> bool:
            if not node:
                return True

            if lower < node.val < upper:
                return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
            else:
                return False

        return dfs(root, -math.inf, math.inf)
        # Time O(n)
        # Space O(h)    = O(log(n)) -> O(n)
