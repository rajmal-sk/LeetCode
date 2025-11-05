class Solution:
    def smallestNumber(self, n: int) -> int:
        s = 0
        i = 0
        while s < n:
            s = (s | (1 << i))
            i += 1
        return s