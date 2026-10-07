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
    public bool IsBalanced(TreeNode root) {
        return GetDepth(root) != -1;
    }

    public int GetDepth(TreeNode root) {
        if (root == null) return 0;

        int leftD = GetDepth(root.left);
        if (leftD == -1) {
            return -1;
        }

        int rightD = GetDepth(root.right);
        if (rightD == -1) {
            return -1;
        }

        if (Math.Abs(leftD - rightD) > 1) {
            return -1;
        }

        return Math.Max(leftD, rightD) + 1;
    }
}
