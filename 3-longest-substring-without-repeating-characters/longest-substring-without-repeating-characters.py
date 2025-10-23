class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mp = {}
        l = res = 0
        for r in range(n):
            if s[r] in mp:
                l = max(mp[s[r]], l)
            mp[s[r]] = r + 1
            res = max(res, r - l + 1)
        return res
        