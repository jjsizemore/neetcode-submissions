from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS - traverse levels with a queue that holds (node, lower, upper) bounds set by ancestors
        q = deque()

        q.append((root, -math.inf, math.inf))

        while q:
            cur, lower, upper = q.popleft()

            if not (lower < cur.val < upper):
                return False

            if cur.left:
                q.append((cur.left, lower, cur.val))
            if cur.right:
                q.append((cur.right, cur.val, upper))

        return True
