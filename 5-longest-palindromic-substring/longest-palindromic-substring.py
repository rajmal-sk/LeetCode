class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1: right]


        for i in range(len(s)):
            
            # Odd Length
            oddPalindrome = expand(i, i)
            evenPalindrome = expand(i, i + 1)

            longPalindrome = oddPalindrome if len(oddPalindrome) > len(evenPalindrome) else evenPalindrome
            if len(longPalindrome) > len(res):
                res = longPalindrome

        return res