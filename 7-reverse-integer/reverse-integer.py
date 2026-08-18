class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        
            
        res = 0
        while x > 0:
            lastdigit = x % 10
            x = x // 10
            if res > (2**31 - 1 - lastdigit) // 10:
                return 0

            res = res * 10 + lastdigit 
            
        
        res = res * sign
        return res


        
        