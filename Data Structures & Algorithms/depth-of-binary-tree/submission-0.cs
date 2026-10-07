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
    public int MaxDepth(TreeNode root) {
        // basecase null return 0
        if (root == null) return 0;

        // recurse return 1 + Max(MaxDepth(l), MaxDepth(r))
        return 1 + Math.Max(MaxDepth(root.left), MaxDepth(root.right));
    }
}
