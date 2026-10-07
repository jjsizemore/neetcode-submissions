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

    public int MaxD = 0;

    public int DiameterOfBinaryTree(TreeNode root) {
        GetDepth(root);
        return MaxD;
    }

    public int GetDepth(TreeNode node) {
        if (node == null) return 0;

        int lDepth = GetDepth(node.left);
        int rDepth = GetDepth(node.right);

        MaxD = Math.Max(MaxD, lDepth + rDepth);

        return Math.Max(lDepth, rDepth) + 1;
    }
}
