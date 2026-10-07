public class KthLargest {
    // Can use a MinHeap
    // Remove all but k elems, and elem at idx 0 will be kth largest

    private PriorityQueue<int, int> pq;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.pq = new();
        this.k = k;
        
        foreach (int num in nums) {
            pq.Enqueue(num,num);
            if (pq.Count > k) pq.Dequeue();
        }
    }
    
    public int Add(int val) {
        pq.Enqueue(val, val);

        if (pq.Count > k) pq.Dequeue();

        return pq.Peek();
    }
}
