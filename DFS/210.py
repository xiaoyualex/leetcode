class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        res = []
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
        
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            res.append(i)
            return True
                    
        
        for i,j in prerequisites:
            graph[i].append(j)
        for i in range(numCourses):
            
            if not dfs(i):
                return []
        return res