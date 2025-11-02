class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        num = x
        while num > 0:
            pop = num % 10
            num = num // 10

            rev = rev * 10 + pop
        
        return rev == x
