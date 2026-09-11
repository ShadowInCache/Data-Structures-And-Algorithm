class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def is_distint(a, b, c, d):
            return a != b and a != c and a != d  and b != c and b != d and c != d
        
        h = {}
        n = len(nums)
        for i in range(n):
            h[nums[i]] = i
        
        s = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    needed = target - nums[i] - nums[j] - nums[k]
                    if needed in h and is_distint(i,j,k,h[needed]):
                        t = tuple(sorted([nums[i], nums[j], nums[k], needed]))
                        s.add(t)
        
        return [list(x) for x in s]