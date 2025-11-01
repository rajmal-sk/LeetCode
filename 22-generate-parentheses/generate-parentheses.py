class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(curr , leftCount, rightCount):
            if len(curr) == 2 * n:
                ans.append("".join(curr))
            
            if leftCount < n:
                curr.append('(')
                backtrack(curr, leftCount + 1, rightCount)
                curr.pop()

            if leftCount > rightCount:
                curr.append(')')
                backtrack(curr, leftCount, rightCount + 1)
                curr.pop()
        
        backtrack([], 0, 0)
        return ans