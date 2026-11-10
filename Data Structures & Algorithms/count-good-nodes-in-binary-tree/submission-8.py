# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS with a helper function that takes in the node and the greatest seen otw to it
        # Increments a nonlocal variable res
        res = 0

        def dfs(node, maxSeen):
            if not node:
                return

            nonlocal res

            if node.val >= maxSeen:
                res += 1
                maxSeen = node.val

            dfs(node.left, maxSeen)
            dfs(node.right, maxSeen)

        dfs(root, root.val)

        return res

    # Time O(n)
    # Space O(h) = O(n) -> O(log(n)) best to worst, balanced to degenerate
