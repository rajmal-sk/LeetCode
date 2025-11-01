class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def valid(row, col):
            ch = board[row][col]
            board[row][col] = "."

            for i in range(0, 9):
                # Check Rows
                if board[i][col] == ch:
                    return False
                
                # Check Columns
                if board[row][i] == ch:
                    return False
                
                # Check 3 * 3 square
                if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == ch:
                    return False
            
            board[row][col] = ch
            return True


        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    # valid is a helper function to check if a particular
                    # elments at row, cal is not duplicate within the specific bounds
                    if not valid(i, j):
                        return False
        
        return True
