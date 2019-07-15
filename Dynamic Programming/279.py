class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [i for i in range(n+1)]
        squares = [i**2 for i in range(1,int(n**0.5)+1)]
        for x in range(1,n+1):
            for y in squares:
                if x < y:
                    break
                else:
                    dp[x] = min(dp[x],dp[x-y]+1)
        return dp[-1]