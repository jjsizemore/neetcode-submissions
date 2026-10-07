public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        // MinHeap with k elems, removing every time Count > k
        // Elem at front will be kth largest elem
        var minHeap = new PriorityQueue<int, int>();

        foreach (int num in nums) {
            minHeap.Enqueue(num, num);

            if (minHeap.Count > k) {
                minHeap.Dequeue();
            }
        }

        return minHeap.Peek();
    }
}
