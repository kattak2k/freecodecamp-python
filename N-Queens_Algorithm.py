def dfs_n_queens(n):
    # Requirement: return empty list if n < 1
    if n < 1:
        return []
    
    solutions = []
    
    def is_valid(board, row, col):
        for i in range(row):
            # Check column and both diagonals
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row, board):
        # Base case: All queens are placed
        if row == n:
            solutions.append(list(board))
            return
        
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1, board)
                # Backtracking occurs implicitly as board[row] 
                # is overwritten in the next iteration of col

    # Initialize board with n elements representing row indices
    solve(0, [0] * n)
    return solutions

# 1. You should have a function named dfs_n_queens that takes one argument.
# Passed:2. If n is less than 1, the function should return an empty list.
# Passed:3. The function should return a list of solutions, where each solution is a list of length n.
# Passed:4. dfs_n_queens(1) should return [[0]].
# Passed:5. dfs_n_queens(2) should return [].
# Passed:6. dfs_n_queens(3) should return [].
# Passed:7. dfs_n_queens(4) should return [[1, 3, 0, 2], [2, 0, 3, 1]].
# Passed:8. dfs_n_queens(5) should return [[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]].
# Passed:9. len(dfs_n_queens(5)) should be 10.
# Passed:10. len(dfs_n_queens(8)) should be 92.
# Passed:11. dfs_n_queens should return the correct result.
