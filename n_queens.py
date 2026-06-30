def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    
    def is_safe(current_board, row, col):
        for r in range(row):
            c = current_board[r]
        
            if c == col:
                return False
           
            if abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(row, current_board):
       
        if row == n:
            solutions.append(list(current_board))
            return
        
       
        for col in range(n):
            if is_safe(current_board, row, col):
                current_board[row] = col
                backtrack(row + 1, current_board)
               

    backtrack(0, [0] * n)
    return solutions