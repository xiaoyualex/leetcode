class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        balance = 0
        position = 0
        gap = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                gap -= balance
                balance = 0
                position = i+1
        if position >= len(gas) or balance < gap:
            return -1
        else:
            return position