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
    public int MaxHeight(TreeNode root) {
        // base case null return 0
        if (root == null) return 0;

        // recurse relation return 1 + max of l and r heights
        return Math.Max(MaxHeight(root.left), MaxHeight(root.right)) + 1;
    }

    public int DiameterOfBinaryTree(TreeNode root) {
        // base case null returns 0
        if (root == null) return 0;

        int d = MaxHeight(root.left) + MaxHeight(root.right);

        int dSubtree = Math.Max(DiameterOfBinaryTree(root.left),
                                DiameterOfBinaryTree(root.right));


        return Math.Max(d, dSubtree);
    }
}
