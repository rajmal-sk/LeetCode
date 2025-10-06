class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack(curr):
            # Base Condition - Terminating Condition
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack(curr)
        return ans