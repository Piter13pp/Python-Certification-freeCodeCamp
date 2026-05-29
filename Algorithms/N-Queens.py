def dfs_n_queens(n):
    if n < 1:
        return []
    result = []

    def isSafe(board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def goBack(row, board):
        if row == n:
            result.append(list(board))
            return

        for col in range(n):
            if isSafe(board, row, col):
                board[row] = col
                goBack(row + 1, board)

    goBack(0, [-1] * n)
    return result

def Visualize(board):
    n = len(board)
    for row in range(n):
        line = ''
        for col in range(n):
            if board[row] == col:
                line += 'Q '
            else:
                line += '. '
        print(line)
    print()

n = 4
print(dfs_n_queens(n))
n_solutions = len(dfs_n_queens(n))
print(f"Total number of solutions for {n} queens: {n_solutions}\n")

if n_solutions > 0:
    print("Visualize solutions? (y/n)")
    choice = input().lower()
    if choice == 'y':
        for i, solution in enumerate(dfs_n_queens(n), start=1):
            print(f"Solution #{i}:")
            Visualize(solution)
    elif choice == 'n':
        print("~ Okay, your choice.")