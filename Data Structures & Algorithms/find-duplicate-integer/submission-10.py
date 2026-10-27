class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # can treat the list as a linked list, where the value at some idx i points to another node
        # starting at the first val, save the val, set nums[idx] = 0, 
        # move on to the val at idx = val
        # at any point if the val is already 0, that val is the dupe

        idx = 0

        while True:
            if nums[idx] == 0:
                return idx

            val = nums[idx]
            nums[idx] = 0
            idx = val
        
        return -1
