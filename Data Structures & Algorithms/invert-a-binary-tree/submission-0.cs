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
    public TreeNode InvertTree(TreeNode root) {
        // Basecase: node null, return null

        // Recurse: call on children, swap children, return self
        if (root == null) return null;

        var ptr = InvertTree(root.right);
        root.right = InvertTree(root.left);
        root.left = ptr;

        return root;
    }
}
