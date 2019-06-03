class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newtail = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[newtail]:
                newtail += 1
                nums[newtail] = nums[i]
        return newtail+1
                