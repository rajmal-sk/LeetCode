class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def compress(s: str)-> str:
            freq = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                freq[idx] += 1

            res= ""
            for idx, val in enumerate(freq):
                if val > 0:
                    res += chr(ord('a') + idx) + f"{val}"
            return res

        mp = defaultdict(list)
        for s in strs:
            key = compress(s)
            mp[key].append(s)
        
        res = []
        for value in mp.values():
            res.append(value)
        
        return res