class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax = nums[0]
        curMin = nums[0]
        res =nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                curMax, curMin = curMin, curMax
            
            curMax = max(num, curMax * num)
            curMin = min(num, curMin * num)

            res = max(res, curMax)
        
        return res
        