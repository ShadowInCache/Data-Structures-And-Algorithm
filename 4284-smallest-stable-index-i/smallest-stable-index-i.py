class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        score = 0
        maxNum = nums[0]

        for i in range(n):
            maxNum = max(maxNum, nums[i])
            minNum = min(nums[i:n])

            score = maxNum - minNum

            if score <= k:
                return i

        return -1