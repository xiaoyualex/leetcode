class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numbers = []
    
        
        for token in tokens:
            if token not in ['+','/','*','-']:
                numbers.append(int(token))
            else:
                r, l = numbers.pop(),numbers.pop()
                if token == '+':
                    res = l+r
                elif token == '-':
                    res = l-r
                elif token == '*':
                    res = l*r
                else:
                    if l*r < 0 and l%r != 0:
                        res = l/r + 1
                    else:
                        res = l/r
                numbers.append(res)
        return numbers.pop()
            