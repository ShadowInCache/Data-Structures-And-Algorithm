class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        leftmax = 0
        rightmax = 0
        water = 0

        while (l < r):
            if (height[l] < height[r]):
                leftmax = max(leftmax, height[l])
                water += leftmax - height[l]
                l+=1
            else:
                rightmax = max(rightmax, height[r])
                water += rightmax - height[r]
                r-=1
        
        return water