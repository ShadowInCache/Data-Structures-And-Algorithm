class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums):
            return -1
        
        count = {}
        n = len(nums)

        # Check every subarray of size k
        for i in range(n - k + 1):

            # Store unique elements of current subarray
            seen = {}

            for j in range(i, i + k):
                x = nums[j]
                seen[x] = 1

            # Count how many subarrays contain each number
            for x in seen:
                count[x] = count.get(x, 0) + 1

        # Find largest number that appears in exactly one subarray
        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans