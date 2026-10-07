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
    public List<List<int>> LevelOrder(TreeNode root) {
        var retVal = new List<List<int>>();
        if (root == null) return retVal;

        var q = new Queue<TreeNode>();
        q.Enqueue(root);

        while (q.Count > 0) {
            var level = new List<int>();
            int levelCount = q.Count;

            for (int i = 0; i < levelCount; i++) {
                var cur = q.Dequeue();

                if (cur.left != null) q.Enqueue(cur.left);
                if (cur.right != null) q.Enqueue(cur.right);
                
                level.Add(cur.val);
            }

            retVal.Add(level);
        }

        return retVal;
    }
}
