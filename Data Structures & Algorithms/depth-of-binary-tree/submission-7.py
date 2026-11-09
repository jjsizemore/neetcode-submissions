from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive BFS
        if not root:
            return 0

        q = deque()
        q.append(root)
        maxDepth = 0

        while q:
            size = len(q)
            maxDepth += 1

            for _ in range(size):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return maxDepth
