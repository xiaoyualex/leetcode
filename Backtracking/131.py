class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if not s:
            return result
        self.helper(s,result,[])
        return result
    
    def helper(self,s,result,path):
        if not s:
            result.append(path)
            return 
        for i in range(len(s)):
            if self.isPal(s[:i+1]):
                self.helper(s[i+1:],result,path+[s[:i+1]])
    
    
    def isPal(self,s):
        if s == s[::-1]:
            return True
        
        