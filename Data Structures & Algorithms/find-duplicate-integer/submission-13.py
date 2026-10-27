class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # can treat the list as a linked list, where the value at some idx i points to another node
        # traverse with slow & fast pointer cycle algo 
        # traverse links by going from idx to idx by going from idx to nums[idx]

        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break


        ptr_from_start = 0
        ptr_from_meeting = slow

        while ptr_from_start != ptr_from_meeting:
            ptr_from_start = nums[ptr_from_start]
            ptr_from_meeting = nums[ptr_from_meeting]

        return ptr_from_start
