def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    if row == n:
        print("Final N-Queens Solution Matrix:")
        print_solution(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0
    
    return False

n = int(input("Enter value of n: "))
r = int(input("Enter row index of first queen (0 to n-1): "))
c = int(input("Enter column index of first queen (0 to n-1): "))

board = [[0 for _ in range(n)] for _ in range(n)]

board[r][c] = 1

if not solve_nqueens(board, r + 1, n):
    print("No solution exists for this placement.")
