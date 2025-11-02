class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
        left = 0
        right = l -1
        while(left < right):
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
