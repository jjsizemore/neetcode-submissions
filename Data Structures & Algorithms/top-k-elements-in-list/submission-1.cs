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

        for (int j = freq.Length - 1; j >= 0; j--) {
            foreach (int val in freq[j]) {
                retVal[--k] = val;
                if (k == 0) return retVal;
            }
        }
        return retVal;
    }
}
