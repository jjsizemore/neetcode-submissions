# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # DFS without idx map -- use dfs helper function with a limit parameter
        # Hitting the limit in inorder tells us that a subtree is done
        # Preorder idx tells us which node to create next

        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return
            
            if inorder[inIdx] == limit:
                inIdx += 1
                return None
        
            val = preorder[preIdx]
            root = TreeNode(val)
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root

        return dfs(math.inf)