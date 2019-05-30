class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[0 for i in range(n)] for j in range(m)]
        result[0][0] = 1 - obstacleGrid[0][0]
        for j in range(1,n):
            result[0][j] = result[0][j-1]*(1-obstacleGrid[0][j])
        for i in range(1,m):
            result[i][0] = result[i-1][0]*(1-obstacleGrid[i][0])
        
            
        for i in range(1,m):
            for j in range(1,n):
                result[i][j] = (result[i-1][j] + result[i][j-1])*(1 - obstacleGrid[i][j])
        return result[-1][-1]
        
        