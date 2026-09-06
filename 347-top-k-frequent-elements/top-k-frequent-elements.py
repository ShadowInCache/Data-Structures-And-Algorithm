class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        counter = Counter(nums)
        bucket = [0] * (n+1)

        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
            
        res = []
        for i in range(n, 0, -1):
            if bucket[i] != 0:
                res.extend(bucket[i])
            if len(res) == k:
                return res