class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # netCost = [ gas[i] - cost[i] for i in range(n)]
        prefixSum = 0
        currSum = 0
        l = r = 0
        for r in range(n):
            currSum = currSum + (gas[r] - cost[r])
            if currSum < 0:
                prefixSum = prefixSum + currSum
                currSum = 0
                l = r + 1
        
        return -1 if currSum + prefixSum < 0 else l