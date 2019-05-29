class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
    
        curSum = [0]*len(nums)
        curSum[0] = nums[0]
        for i in range(1,len(nums)):
            curSum[i] = max(nums[i],curSum[i-1]+nums[i])
        return max(curSum)