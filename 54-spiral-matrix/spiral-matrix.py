class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        res = []
        n = row * col

        up = 0
        down = row - 1
        left = 0
        right = col -1

        while len(res) < n:
            # Traverse from left to right - row constant , col changes
            for c in range(left, right + 1):
                res.append(matrix[up][c])
            
            # Traverse from top to bottom - row changes, col constant
            for r in range(up + 1, down + 1):
                res.append(matrix[r][right])
            

            # Traverse from right to left - row constant, col changes
            # But check for if we have already visited the row 

            if up != down:
                for c in range(right - 1, left - 1, - 1):
                    res.append(matrix[down][c])

            # Traverse from bottom to top - row changes, col constant
            # But check for if we have already visited the col

            if left != right:
                for r in range(down - 1, up, - 1):
                    res.append(matrix[r][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return res
