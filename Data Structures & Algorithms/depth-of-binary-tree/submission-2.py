# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive helper
        # takes in cur node and cur level, starting with 1 at root
        # level does up for each non-None node
        # base case is node is None, return level
        # return recursive call at bottom
        return self._helper(root)
    
    def _helper(self, cur, level: int = 0) -> int:
        if not cur:
            return level

        level += 1
        
        return max(self._helper(cur.left, level), self._helper(cur.right, level))