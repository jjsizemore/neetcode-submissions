from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS, at each level, take the last value from the queue as the rightmost
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []

        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res

