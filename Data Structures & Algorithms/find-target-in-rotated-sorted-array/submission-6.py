class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # need to find pivot point
        # if nums[mid] > nums[r], l = mid + 1
        # else r = mid

        l, r = 0, len(nums) - 1
        mid = 0
        while l < r:
            mid = (r - l) // 2 + l

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        print(f'Pivot idx is {pivot}\nValue is {nums[pivot]}')
        
        if nums[pivot] <= target and target <= nums[-1]:
            l, r = pivot, len(nums) - 1
        elif nums[0] <= target and target <= nums[pivot - 1]:
            l, r = 0, pivot - 1
        else:
            return -1

        while l <= r:
            mid = (r - l) // 2 + l
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1