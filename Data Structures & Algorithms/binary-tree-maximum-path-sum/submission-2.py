# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 3 scenarios at each node
        # path incl l & r subtrees
        # only 1 subtree
        # path from parent (should have been computed when traversing parent)
        # DFS traverse
        
        res = -math.inf

        # return best downward path to parent

        def dfs(node):
            if not node:
                return 0

            nonlocal res
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            oneSide = max(leftSum, rightSum) + node.val
            bothSides = leftSum + rightSum + node.val

            res = max(bothSides, oneSide, node.val, res)

            return max(0, leftSum, rightSum) + node.val

        dfs(root)

        return res
