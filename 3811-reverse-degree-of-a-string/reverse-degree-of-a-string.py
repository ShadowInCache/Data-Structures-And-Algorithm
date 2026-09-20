class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        reverse = 0

        for i in range(len(s)):
            reverse += (ord('z') - ord(s[i]) + 1) * (i+1)
            
        return reverse
