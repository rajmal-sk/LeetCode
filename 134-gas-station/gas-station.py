class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        netCost = [ gas[i] - cost[i] for i in range(n)]
        prefixSum = 0
        currSum = 0
        l = r = 0
        for r in range(n):
            currSum = currSum + netCost[r]
            if currSum < 0:
                prefixSum = prefixSum + currSum
                currSum = 0
                l = r + 1
        
        if currSum + prefixSum >= 0:
            return l
        else :
            return -1