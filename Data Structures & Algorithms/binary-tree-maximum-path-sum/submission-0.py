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

        def dfs(node, curSum):
            if not node:
                return 0

            nonlocal res
            
            leftSum = dfs(node.left, 0)
            rightSum = dfs(node.right, 0)

            lr = leftSum + rightSum + node.val
            l = leftSum + node.val + curSum
            r = rightSum + node.val + curSum
            n = curSum + node.val

            res = max(lr, l, r, n, res)

            return max(0, leftSum, rightSum) + n

        dfs(root, 0)

        return res
