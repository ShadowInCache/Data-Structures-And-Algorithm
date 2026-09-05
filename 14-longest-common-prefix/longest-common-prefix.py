class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return prefix
            
            prefix += char
        return prefix