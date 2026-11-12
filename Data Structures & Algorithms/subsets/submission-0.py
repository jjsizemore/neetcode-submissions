class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # For each number, need to find the subsets that include the number and that don't
        # backtracking algo
        if not nums:
            return [[]]

        return self._backtrack(nums, [[]])

    def _backtrack(self, nums: List[int], subsets: List[List[int]]) -> List[List[int]]:
        if not nums:
            return

        temp = []
        for subset in subsets:
            temp.append(subset + [nums[0]])

        subsets.extend(temp)

        if len(nums) > 1:
            self._backtrack(nums[1:], subsets)
        
        return subsets
        