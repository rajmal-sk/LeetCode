class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations) # Represents the max value of h-index
        hIdx = 0
        for i in range(1, n + 1):
            # Check if i papers are available with atleast i citations
            count = 0
            for j in range(n):
                if citations[j] >= i:
                    count += 1
            
            if count >= i:
                hIdx = i
        return hIdx