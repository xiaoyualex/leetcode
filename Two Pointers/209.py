class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        summ = 0
        minLength = len(nums)+1
        for i in range(len(nums)):
            summ += nums[i]
            while summ >= s:
                minLength = min(minLength,i-start+1)
                summ -= nums[start]
                start += 1
        return minLength if minLength < len(nums)+1 else 0