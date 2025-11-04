class Solution:
    def minOperations(self, n: int) -> int:
        powers = [1 << i for i in range(int(log2(n)) + 2)]
        
        count = 0

        while n:
            min_diff = float('inf')
            closest = n
            for pow in powers:
                if abs(pow - n) < min_diff:
                    min_diff = abs(pow - n)
                    closest = pow
            
            n = abs(n - closest)
            count += 1

        return count