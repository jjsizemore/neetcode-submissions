public class Solution {
    public int LastStoneWeight(int[] stones) {
        var heap = new PriorityQueue<int, int>();

        foreach (var wt in stones) {
            heap.Enqueue(wt, -wt);
        }

        while (heap.Count > 1) {
            int heaviest = heap.Dequeue();
            int secondHeaviest = heap.Dequeue();

            if (heaviest == secondHeaviest) continue;
            
            int newWeight = heaviest - secondHeaviest;
            heap.Enqueue(newWeight, -newWeight);
        }

        return heap.Count > 0 ? heap.Peek() : 0;
    }

}
