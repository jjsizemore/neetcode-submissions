public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> count = new();
        List<int>[] freq = new List<int>[nums.Length + 1];

        for (int i = 0; i < freq.Length; i++)
            freq[i] = new List<int>();
        
        foreach (int n in nums) {
            if (!count.ContainsKey(n))
                count[n] = 0;
            count[n]++;
        }

        foreach (var pair in count) {
            freq[pair.Value].Add(pair.Key);
        }

        var retVal = new int[k];
        int idx = 0;
        for (int i = freq.Length - 1; i >= 0; i--) {
            foreach (int val in freq[i]) {
                retVal[idx++] = val;
                if (idx >= k) return retVal;
            }
        }
        return retVal;
    }
}
