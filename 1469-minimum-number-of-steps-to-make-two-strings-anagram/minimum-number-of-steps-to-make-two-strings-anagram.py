class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mp_s = Counter(s)
        mp_t = Counter(t)

        count = 0
        for key, value in mp_t.items():
            if key not in mp_s:
                count += value
            
            else:
                if value <= mp_s[key]:
                    mp_s[key] -= value
                else:
                    count += (value - mp_s[key])
                    mp_s[key] = 0
        return count
        
        return 0