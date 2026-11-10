# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS helper function with a nonlocal res & count variables
        # Base case, if node is null return -1
        # Do typical left right dfs, at first node where .left call returns -1, set res to cur.val, increment count, and return -1 so that the parent caller knows to run on its node next
        # Once count = k, short circuit to return res up the chain

        res, count = 0, 0

        # returns -1 while searching and returns k-th smallest otherwise
        def dfs(cur) -> int:
            if not cur:
                return -1
            
            left = dfs(cur.left)
            if left != -1:
                return left
            else:
                nonlocal res
                nonlocal count
                res = cur.val
                count += 1
                if count == k:
                    return res
                
                right = dfs(cur.right)

                if right != -1:
                    return right

            return -1

        return dfs(root)