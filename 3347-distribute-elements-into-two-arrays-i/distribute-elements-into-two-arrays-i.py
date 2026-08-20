class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Arr1 = []
        Arr2 = []

        Arr1.append(nums[0])
        Arr2.append(nums[1])

        for i in range(2, len(nums)):
            if Arr1[-1] > Arr2[-1]:
                Arr1.append(nums[i])
                
            else:
                Arr2.append(nums[i])
                
        return Arr1 + Arr2