class Solution:
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        n = len(target)

        # Try to match target from left to right
        for i in range(n):
            x = ord(target[i]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
        else:
            # target itself can be formed.
            # Need to find the next permutation by backtracking.
            i = n

        # First, try to make the string greater at the
        # position where matching failed.
        if i < n:
            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    suffix = ""
                    for k in range(26):
                        suffix += chr(k + ord('a')) * cnt[k]

                    return target[:i] + chr(c + ord('a')) + suffix

        # We couldn't make it greater at i.
        # Backtrack through the matched prefix.
        for j in range(i - 1, -1, -1):
            x = ord(target[j]) - ord('a')

            # Put target[j] back into available characters
            cnt[x] += 1

            # Find the smallest character greater than target[j]
            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    suffix = ""
                    for k in range(26):
                        suffix += chr(k + ord('a')) * cnt[k]

                    return (
                        target[:j]
                        + chr(c + ord('a'))
                        + suffix
                    )

        return ""