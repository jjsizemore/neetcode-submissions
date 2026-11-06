# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative DFS - explicit stack instead of recursion
        # 1. visit node
        # 2. swap node's children
        # 3. do 1 & 2 for node's children

        stack = []
        stack.append(root)

        while stack:
            cur = stack.pop()
            if not cur:
                continue

            old_left = cur.left
            old_right = cur.right

            cur.left = old_right
            cur.right = old_left

            stack.append(cur.left)
            stack.append(cur.right)
        
        return root

        # Space O(n) where n = # nodes
        # Time O(n) for stack if tree is completely imbalanced
