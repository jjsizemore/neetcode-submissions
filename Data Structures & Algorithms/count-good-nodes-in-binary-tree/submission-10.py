from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS - traverse by level, carry max val so far for each path
        q = deque()

        q.append((root, root.val))

        res = 0

        while q:
            cur, maxSeen = q.popleft()

            if cur.val >= maxSeen:
                res += 1
                maxSeen = cur.val

            if cur.left:
                q.append((cur.left, maxSeen))
            if cur.right:
                q.append((cur.right, maxSeen))
        
        return res
        # Time O(n)
        # Space O(n)
            