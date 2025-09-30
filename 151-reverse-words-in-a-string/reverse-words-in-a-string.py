class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)
        res = ""
        for i in range(n - 1, -1, -1):
            if i!= 0:
                res += words[i] + " "
            elif i == 0:
                res += words[i]
        return res
