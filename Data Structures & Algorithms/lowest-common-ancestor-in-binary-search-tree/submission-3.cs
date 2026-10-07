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
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // can use binary search tree structure to speed things up
        // LCA if 
        //  one target in one sub and (one in other or self)
        //  meaning (bot <= root && root <= top)


        var top = p.val > q.val ? p : q;
        var bot = top == p ? q : p;

        while (root != null) {
            if (root.val > top.val) {
                root = root.left;
            } else if (root.val < bot.val) {
                root = root.right;
            } else {
                // bot.val <= root.val <= top.val
                return root;
            }
        }

        return null;
    }
}
