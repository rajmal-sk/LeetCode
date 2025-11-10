class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(row, diag, antidiag, cols):
            if row == n:
                return 1

            ans = 0

            for col in range(n):
                diagonal = row - col
                antidiagonal = row + col

                if (col in cols or 
                diagonal in diag or 
                antidiagonal in antidiag):
                    continue
                
                cols.add(col)
                diag.add(diagonal)
                antidiag.add(antidiagonal)

                ans += backtrack(row + 1, diag, antidiag, cols)

                cols.remove(col)
                diag.remove(diagonal)
                antidiag.remove(antidiagonal)
            
            return ans
        
        return backtrack(0, set(), set(), set())
