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
    public int retVal = 0;
    public int DiameterOfBinaryTree(TreeNode root) {
        GetDiameter(root);
        return retVal;
    }

    public int GetDiameter(TreeNode root) {
        if (root == null) return 0;

        int leftDiameter = GetDiameter(root.left);
        int rightDiameter = GetDiameter(root.right);

        int currentDiameter = leftDiameter + rightDiameter;
        retVal = Math.Max(retVal, currentDiameter);

        return Math.Max(leftDiameter, rightDiameter) + 1;
    }
}
