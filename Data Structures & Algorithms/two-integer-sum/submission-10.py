class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, cur in enumerate(nums):
            compl = target - cur

            if compl in seen:
                return [seen[compl], i]
            
            seen[cur] = i
        
        return []