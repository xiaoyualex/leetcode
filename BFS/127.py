class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList:
            return 0
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        q = [(beginWord,1)]
        alpha_list = 'abcdefghijklmnopqrstuvwxyz'
        visit_set = set()
        while q:
            word, length = q.pop(0)
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in alpha_list:
                    new_word = word[:i]+ch+word[i+1:]
                    
                    if new_word in wordList and new_word not in visit_set:
                        q.append((new_word,length+1))
                        visit_set.add(new_word)
        return 0
                