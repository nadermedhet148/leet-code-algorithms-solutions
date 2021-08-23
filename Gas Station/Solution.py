from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        totalGas , start = 0,0
        for i in range(len(gas)):
            totalGas = (gas[i] + totalGas) - cost[i]
        
            if totalGas < 0:
                start = i + 1
                totalGas = 0

        return start


s = Solution()
print(
s.canCompleteCircuit(gas = [5,1,3,2,4], cost = [3,4,1,5,2])
)