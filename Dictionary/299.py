class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0 
        cow = 0
        
        dic1 = {}
        dic2 = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            dic1[secret[i]] = dic1.get(secret[i],0) + 1
            dic2[guess[i]] = dic2.get(guess[i],0) + 1
        for k in dic1:
            if k in dic2:
                cow += min(dic2[k],dic1[k])
        cow -= bull
        return str(bull)+'A'+str(cow)+'B'
            
                