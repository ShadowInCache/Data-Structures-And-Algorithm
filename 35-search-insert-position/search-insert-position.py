class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        res = 0

        while(left <= right):
            mid = (left+right) // 2

            if target > nums[right]:
                return right + 1
            if target < nums[left]:
                return left
            if nums[mid] < target:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        
        return res