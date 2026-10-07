public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        // queue will hold tasks and time that tasks are cooled
        // keep track of time, increment every time we run a task or are idle
        // PQ will hold frequencies and function as a max heap
        // tally freqs in a dict

        var nextWork = new PriorityQueue<int, int>();
        int time = 0;
        var cooldown = new Queue<(int freq, int aliveTime)>();
        var dict = new Dictionary<char, int>();

        foreach (var t in tasks) {
            dict[t] = dict.GetValueOrDefault(t, 0) + 1;
        }

        foreach (var freq in dict.Values) {
            nextWork.Enqueue(freq, -freq);
        }

        while (nextWork.Count > 0 || cooldown.Count > 0) {
            time++;
            // check cooldown and then process or wait
            if (cooldown.Count > 0 && cooldown.Peek().aliveTime == time) {
                var (freq, _) = cooldown.Dequeue();
                nextWork.Enqueue(freq, -freq);
            }

            if (nextWork.Count > 0) {
                var workFreq = nextWork.Dequeue();
                workFreq--;

                if (workFreq > 0) {
                    cooldown.Enqueue((workFreq, time + n + 1));
                }
            }
        }

        return time;
    }
}
