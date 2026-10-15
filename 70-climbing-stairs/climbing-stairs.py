class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur, prev = 1, 1
        for _ in range(n - 1):
            prev, cur = cur , prev + cur
        return cur