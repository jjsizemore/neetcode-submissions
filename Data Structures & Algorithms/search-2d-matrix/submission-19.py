class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search for correct row
        # valid row should have row[0] <= target and row[-1] >= target
        # if row[0] > target, r = mid - 1
        # if row[-1] < target, l = mid + 1
        # if l > r before break, return False
        # simple binary search on row for value


        l, r = 0, len(matrix) - 1
        row = []

        while l <= r:
            mid = (r - l) // 2 + l
            row = matrix[mid]

            if row[0] > target:
                r = mid - 1
            elif row[-1] < target:
                l = mid + 1
            else:
                break

        if l > r:
            return False
        
        l, r = 0, len(row) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            val = row[mid]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
