/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public int DiameterOfBinaryTree(TreeNode root) {
        int MaxD = 0;
        GetDepth(root, ref MaxD);
        return MaxD;
    }

    public int GetDepth(TreeNode node, ref int MaxD) {
        if (node == null) return 0;

        int lDepth = GetDepth(node.left, ref MaxD);
        int rDepth = GetDepth(node.right, ref MaxD);

        MaxD = Math.Max(MaxD, lDepth + rDepth);

        return Math.Max(lDepth, rDepth) + 1;
    }
}
