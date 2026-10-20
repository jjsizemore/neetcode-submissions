class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) == h, k = max(piles) at most
        # l, r = 1, max(piles)

        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (r - l) // 2 + l
            time_eating = 0
            for p in piles:
                time_eating += math.ceil(p / mid)
            if time_eating > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
                
        return res