class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Iterate only the edge of the board
        # If "O" occurs do dfs and capture the (row, col) in seen
            # - seen contains all the (row, col) which are "0" and the region has an "0" on the edge
        
        # Traverse the matrix and if the cell is "0" check if (row, col) in seen:
            # if not - Mark "X"
            # else - move to next cell in the matrix.

        m = len(board)
        n = len(board[0])


        seen = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def dfs(row, col):
            for dx, dy in directions:
                nrow, ncol = row + dx, col + dy
                if (nrow, ncol) not in seen and isValid(nrow, ncol) and board[nrow][ncol] == "O":
                    seen.add((nrow, ncol))
                    dfs(nrow, ncol)

        for row in range(m):
            for col in range(n):
                if row == 0 or row == m -1 or col == 0 or col == n - 1:
                    if board[row][col] == "O" and (row, col) not in seen:
                        seen.add((row, col))
                        dfs(row, col)
        
        for row in range(m):
            for col in range(n):
                if (row, col) not in seen and board[row][col] == "O":
                    board[row][col] = "X"