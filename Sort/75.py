class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0 
        k = 0
        for i in range(len(nums)):
            v = nums[i]
            nums[i] = 2
            if  v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[k] = 0
                k += 1
       