# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Can be a recursive call on root's children, checking if subRoot is inside either
        # If either subtree returns true, return true, otherwise, check the tree starting at root

        if not root:
            return False

        return (self.isSameTree(root, subRoot) or 
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))

    def isSameTree(self, r1, r2) -> bool:
        if not r1 and not r2:
            return True
        if r1 and r2 and r1.val == r2.val:
            return self.isSameTree(r1.left, r2.left) and self.isSameTree(r1.right, r2.right)
        else:
            return False