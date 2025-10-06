class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(path, curr, index):
            if curr == target:
                ans.append(path[ : ])
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num + curr <= target:
                    path.append(num)
                    backtrack(path, num + curr, i)
                    path.pop()
        
        backtrack([], 0 , 0)
        return ans