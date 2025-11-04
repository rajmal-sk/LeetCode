class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 1
        total = 0

        while n > 0:

            # We iterate either 7 days or n depending on which is minimum
            for day in range(min(n, 7)):
                total += monday + day
            
            n -= 7
            monday += 1
        
        return total