class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not candidates:
            return res
        candidates.sort()
        self.helper(candidates,res,[],target,0)
        return res
    
    def helper(self,candidates,res,path,target,index):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(index,len(candidates)):
            if target < candidates[i]:
                break
            self.helper(candidates,res,path+[candidates[i]],target-candidates[i],i)