def solution(rows, columns, queries):
    answer = list()
    board = [[row * columns + i + 1 for i in range(columns)] for row in range(rows)]

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        pivot = board[x1][y1]
        min_num = rows * columns
        for i in range(x1, x2):
            min_num = min(min_num, board[i][y1])
            board[i][y1] = board[i + 1][y1]
        for i in range(y1, y2):
            min_num = min(min_num, board[x2][i])
            board[x2][i] = board[x2][i + 1]
        for i in range(x2, x1, -1):
            min_num = min(min_num, board[i][y2])
            board[i][y2] = board[i - 1][y2]
        for i in range(y2, y1, -1):
            min_num = min(min_num, board[x1][i])
            board[x1][i] = board[x1][i - 1]
        board[x1][y1 + 1] = pivot
        answer.append(min_num)

    return answer