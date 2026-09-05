class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr1 = []
        arr2 = []

        for i in range(len(nums)):
            if nums[i] != 0:
                arr2.append(nums[i])
            else:
                arr1.append(nums[i])

        arr = arr2 + arr1
        nums[:] = arr
        return arr