class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            cur = nums[i]
            compl = target - cur

            if compl in seen:
                return [seen[compl], i]
            
            seen[cur] = i
        
        return