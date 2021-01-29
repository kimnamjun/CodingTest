import copy

def solution(m, n, board):
    board2 = [list() for _ in range(n)]
    for col in range(m-1, -1, -1):
        for row in range(n):
            board2[row].append(board[col][row])

    loop = True
    while loop:
        loop = False
        board3 = copy.deepcopy(board2)
        for row in range(n-1):
            for col in range(m-1):
                try:
                    if board2[row][col] == board2[row][col+1] == board2[row+1][col] == board2[row+1][col+1]:
                        board3[row][col] = board3[row][col+1] = board3[row+1][col] = board3[row+1][col+1] = ' '
                        loop = True
                except:
                    pass

        for row in range(len(board3)):
            while ' ' in board3[row]:
                board3[row].remove(' ')
        board2 = board3

    return n * m - sum([len(row) for row in board2])