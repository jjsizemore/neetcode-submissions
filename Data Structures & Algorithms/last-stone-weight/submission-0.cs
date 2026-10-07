public class Solution {
    public int LastStoneWeight(int[] stones) {
        var heap = new PriorityQueue<int, int>();

        foreach (var wt in stones) {
            heap.Enqueue(wt, -1 * wt);
        }

        while (heap.Count > 1) {
            int x = heap.Dequeue();
            int y = heap.Dequeue();

            if (x == y) continue;
            heap.Enqueue(x - y, y - x);
        }

        return heap.Count > 0 ? heap.Peek() : 0;
    }

}
