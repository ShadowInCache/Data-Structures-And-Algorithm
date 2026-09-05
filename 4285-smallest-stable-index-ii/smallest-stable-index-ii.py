class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        suffixmin = [0] * n
        suffixmin[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffixmin[i] = min(nums[i], suffixmin[i + 1])
        
        maxNum = nums[0]

        for i in range(n):
            maxNum = max(maxNum, nums[i])
            minNum = suffixmin[i]

            score = maxNum - minNum

            if score <= k:
                return i
            
        return -1