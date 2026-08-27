class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        n = len(height)

        l, r = 0, n-1

        while l < r:
            area = min(height[l], height[r]) * (r - l)

            res = max(res, area)

            if height[l] > height[r]:
                r-=1
            else:    
                l+=1

        return res
