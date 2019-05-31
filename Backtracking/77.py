class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if n <= 0:
            return res
        self.helper(res,[],n,k,1)
        return res
    
    def helper(self,res,path,n,k,index):
        if len(path) == k:
            res.append(path)
        
        for i in range(index,n+1):
            self.helper(res,path+[i],n,k,i+1)