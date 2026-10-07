public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        // Upper bound for rate is (# in biggest pile)/hr
        // Lower bound is 1

        // We're searching for the minimal value for rate
        // If we iterate up from 1 -> Max(piles), summing time for each pile
        //  & checking if totalTime < h, we have O(n * m) in the case 
        //  that the minimal rate is m, where m is Max(piles)
        // We can do a binary search on the range 1 -> Max(piles) to bring
        //  runtime down to O(n*log(m))

        int l = 1;
        int r = piles.Max();

        int res = r;

        while (l <= r)
        {
            // Can do this because r <= 1 million
            int k = (r + l) / 2;
            int totalTime = 0;
            foreach (int num in piles)
            {
                totalTime += (int)Math.Ceiling((decimal)num / k);
            }

            if (totalTime > h)
            {
                l = k + 1;
            }
            else
            {
                res = k;
                r = k - 1;
            }
        }
        return res;
    }
}
