# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.switchChildren(root)
    
    def switchChildren(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return
        
        left = node.left
        right = node.right

        node.left = self.switchChildren(right)
        node.right = self.switchChildren(left)

        return node
        