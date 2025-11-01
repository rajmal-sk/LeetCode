class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Brute Force:
        # For each character at index i - check if there is an index from i + 1 to n, with same character
        # as at index i

        n = len(s)

        # for i in range(n):
        #     flag = True
        #     for j in range(n):
        #         if s[j] == s[i] and j != i:
        #             flag = False
        #             break
            
        #     if flag:
        #         return i
        
        # return -1

        mp = defaultdict(list)

        for i in range(n):
            mp[s[i]].append(i)
        

        for value in mp.values():
            if len(value) == 1:
                return value[0]
        
        return -1

                