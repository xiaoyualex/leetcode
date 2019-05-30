class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        A = [[1]*n]*m
        for i in range(1,m):
            for j in range(1,n):
                A[i][j] = A[i-1][j] + A[i][j-1]
        return A[m-1][n-1]
                