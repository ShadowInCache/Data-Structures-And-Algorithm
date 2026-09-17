class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        ans = n + 1
        total = 0

        dp = [n] * (n + 1)
        left = 0

        for right, x in enumerate(arr):
            total += x

            while total > target:
                total -= arr[left]
                left += 1

            dp[right + 1] = dp[right]

            if total == target:
                length = right - left + 1

                ans = min(ans, length + dp[left])

                dp[right + 1] = min(dp[right + 1], length)

        return -1 if ans == n + 1 else ans