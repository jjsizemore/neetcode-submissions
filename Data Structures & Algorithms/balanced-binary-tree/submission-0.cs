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
    public bool RetVal = true;
    public bool IsBalanced(TreeNode root) {
        GetDepth(root);
        return RetVal;
    }

    public int GetDepth(TreeNode root) {
        if (root == null) return 0;
        if (!RetVal) return 0;

        int leftD = GetDepth(root.left);
        int rightD = GetDepth(root.right);

        if (Math.Abs(leftD - rightD) > 1) {
            RetVal = false;
        }

        return Math.Max(leftD, rightD) + 1;
    }
}
