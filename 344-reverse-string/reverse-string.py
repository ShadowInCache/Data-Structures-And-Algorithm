class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        l, r = 0, len(s) - 1

        tem = 0
        while(l < r):
            tem = s[l]
            s[l] = s[r]
            s[r] = tem
            l+=1
            r-=1
        
        return tem