def solution(board):
    x = max(board[0])
    for r, row in enumerate(board[1:]):
        for c, col in enumerate(row[1:]):
            if board[r+1][c+1] and board[r][c+1] and board[r+1][c]:
                board[r+1][c+1] = min(board[r][c], board[r][c+1], board[r+1][c]) + 1
        x = max(x, max(board[r+1]))
    return x * x