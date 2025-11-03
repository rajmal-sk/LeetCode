class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ""
        first = strs[0]
        last = strs[len(strs) - 1]

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                res = res + first[i]
            else:
                break
        return res