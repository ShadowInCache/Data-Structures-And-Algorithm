class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[m][n] = True

        # Fill the table from bottom-right to top-left
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                first_match = (
                    i < m and
                    (s[i] == p[j] or p[j] == '.')
                )

                # If next character is '*'
                if j + 1 < n and p[j + 1] == '*':
                    
                    # '*' matches zero characters
                    zero = dp[i][j + 2]

                    # '*' matches one or more characters
                    one_or_more = first_match and dp[i + 1][j]

                    dp[i][j] = zero or one_or_more

                else:
                    # Normal character or '.'
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]