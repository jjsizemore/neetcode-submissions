public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        // MaxHeap with -(dist to origin) as prio, removing if Count > k
        // Remaining k will be k pts with smallest dist to origin
        var maxHeap = new PriorityQueue<int[], double>();

        foreach (var coord in points) {
            double dist = Math.Sqrt(Math.Pow(coord[0], 2) + Math.Pow(coord[1], 2));
            maxHeap.Enqueue(coord, -dist);

            if (maxHeap.Count > k) {
                maxHeap.Dequeue();
            }
        }

        var retVal = new int[k][];

        for (int i = 0; i < k; i++) {
            retVal[i] = maxHeap.Dequeue();
        }

        return retVal;
    }
}
