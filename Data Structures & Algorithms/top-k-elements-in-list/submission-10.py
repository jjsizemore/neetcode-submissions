class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums))]

        for num, count in counts.items():
            buckets[count - 1].append(num)
        
        retVal = []

        for i in range(len(nums) - 1, -1, -1):
            if len(buckets[i]) > 0:
                retVal.extend(buckets[i])
            if len(retVal) == k:
                return retVal
        
        return []