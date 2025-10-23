class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(left, right):
            l, r = left, right
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l + 1: r]


        for i in range(len(s)):
            
            # Odd Length
            oddPalindrome = expand(i, i)
            evenPalindrome = expand(i, i + 1)

            longPalindrome = oddPalindrome if len(oddPalindrome) > len(evenPalindrome) else evenPalindrome
            if len(longPalindrome) > len(res):
                res = longPalindrome

        return res