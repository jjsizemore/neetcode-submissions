public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        // MaxHeap with -(dist to origin) as prio, removing if Count > k
        // Remaining k will be k pts with smallest dist to origin
        var maxHeap = new PriorityQueue<int[], int>();

        foreach (var coord in points) {
            int distSquared = coord[0] * coord[0] + coord[1] * coord[1];
            maxHeap.Enqueue(coord, -distSquared);

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
