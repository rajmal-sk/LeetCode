class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Brute Force:
        # For each character at index i - check if there is an index from i + 1 to n, with same character
        # as at index i

        n = len(s)

        for i in range(n):
            flag = True
            for j in range(n):
                if s[j] == s[i] and j != i:
                    flag = False
                    break
            
            if flag:
                return i
        
        return -1
                