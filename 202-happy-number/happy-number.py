class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sumofsquares(n)

            if n == 1:
                return True
        return False

    def sumofsquares(self, n):
        res = 0

        while n > 0:
            digit = n % 10
            res = res + digit**2
            n = n // 10

        return res