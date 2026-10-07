public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        // tally frequencies in an array
        // add the tasks with -freq prio to a MaxHeap
        // when we complete a task, add it to a cooldown q with a decremented prio
        // if work pq is empty, add ()

        var freqs = new Dictionary<char, int>();
        foreach (var task in tasks) {
            freqs[task] = freqs.GetValueOrDefault(task) + 1;
        }

        var maxHeap = new PriorityQueue<int, int>();

        foreach (var freq in freqs.Values) {
            maxHeap.Enqueue(freq, -freq);
        }

        // tracks frequency and timeUntil to move back to maxHeap
        var cooldown = new Queue<(int freq, int timeUntil)>();

        int time = 0;

        while (maxHeap.Count > 0 || cooldown.Count > 0) {
            time++;

            if (cooldown.Count > 0 && cooldown.Peek().timeUntil == time) {
                var (freq, _) = cooldown.Dequeue();
                maxHeap.Enqueue(freq, -freq);
            }

            if (maxHeap.Count > 0) {
                int freq = maxHeap.Dequeue();
                freq--;

                if (freq > 0) {
                    cooldown.Enqueue((freq, time + n + 1));
                }
            }
        }

        return time;
    }
}
