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
    // Seems like a recursive helper function would be needed to track bounds

    public bool IsValidBST(TreeNode root) {
        return IsValid(root);
    }

    public bool IsValid(TreeNode node, int? min = null, int? max = null) {
        if (node == null) return true;

        if ((min.HasValue && node.val <= min.Value) ||
            (max.HasValue && node.val >= max.Value)) {
                return false;
        }

        // val is max for left and min for right

        return IsValid(node.left, min, node.val) &&
                IsValid(node.right, node.val, max);
    }
}
