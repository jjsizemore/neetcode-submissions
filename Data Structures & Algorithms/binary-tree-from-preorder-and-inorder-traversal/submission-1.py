# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #               1
    #        2              3
    #  4         5       6      7
# preorder  [1,2,3,4,5,6,7]
# inorder   [4,2,5,1,6,3,7]

    #               1
    #        2              3
    #  4                6      7
# preorder  [1,2,3,4,6,7]
# inorder   [4,2,1,6,3,7]

# left = [4,2]
# right = [6,3,7]
#                   1
#                2     3                [4], [6,7]
#              4   6 not here because it's not between 2 and 1 in the inorder

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # preorder allows you to get root node
        # nodes to left in inorder are in the nodes left subtree, right are in the right
        # for each node in preorder array, create node, find idx, recursively build l and r subtrees

        idxs = { val: idx for idx, val in enumerate(inorder) }
        head = TreeNode(preorder[0])

        # track current idx in the pre-order array
        cur_idx = 0

        # DFS helper function that takes in left and right idxs in the inorder array for building a subtree
        def dfs(l, r):
            # node is not in this subtree according to inorder idxs
            if l > r:
                return

            nonlocal cur_idx
            cur_val = preorder[cur_idx]
            cur_idx += 1
            cur = TreeNode(cur_val)

            inorder_idx = idxs[cur_val]
            cur.left = dfs(l, inorder_idx - 1)
            cur.right = dfs(inorder_idx + 1, r)
            
            return cur
        
        return dfs(0, len(inorder) - 1)
