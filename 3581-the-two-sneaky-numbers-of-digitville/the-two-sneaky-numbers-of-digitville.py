class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)
        res = []

        for key, value in mp.items():
            if value == 2:
                res.append(key)


        return res