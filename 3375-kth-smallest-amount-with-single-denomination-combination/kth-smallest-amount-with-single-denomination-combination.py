class Solution:
    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def count(x):
            ans = 0

            for mask in range(1, 1 << len(coins)):
                l = 1
                bits = 0

                for i in range(len(coins)):
                    if mask >> i & 1:
                        bits += 1
                        l = l // gcd(l, coins[i]) * coins[i]

                        if l > x:
                            break

                if l <= x:
                    if bits & 1:
                        ans += x // l
                    else:
                        ans -= x // l

            return ans

        lo = 1
        hi = min(c * k for c in coins)

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo