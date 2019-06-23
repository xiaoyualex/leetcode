class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        r = nums[0]
        Max = [r]
        Min = [r]
        for i,num in enumerate(nums[1:]):
            if num > 0:
                Max.append(max(num,Max[i]*num))
                Min.append(min(num,Min[i]*num))
            else:
                Max.append(max(num,Min[i]*num))
                Min.append(min(num,Max[i]*num))
        return max(Max)