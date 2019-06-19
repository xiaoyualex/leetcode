class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
       
        for i in range(len(s)):
            str1 = s[i:i+10]
            dic[str1] = dic.get(str1,0) + 1
        return [i for i,j in dic.items() if j > 1]