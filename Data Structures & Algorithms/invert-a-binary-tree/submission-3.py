# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS iterative solution
        # BFS typically requires a queue for each level
        # for each node, swap children, then push the new children into a queue

        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()
            if not cur:
                continue
                
            left = cur.left
            right = cur.right

            cur.left = right
            cur.right = left

            q.append(right)
            q.append(left)

        return root
