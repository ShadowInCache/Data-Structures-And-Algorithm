class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i
        
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in d and i != d[x]:
                return [i,d[x]]
        return None