class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        res = 0

        while (left < right):
            if nums[left] < nums[right]:
                right -= 1
            else:
                left += 1
        res += nums[left]

        return res