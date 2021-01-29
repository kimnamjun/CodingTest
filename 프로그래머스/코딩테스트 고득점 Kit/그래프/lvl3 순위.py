def solution(n, results):
    table = [[0 for _ in range(n)] for _ in range(n)]

    for winner, loser in results:
        table[winner-1][loser-1] = 1
        table[loser-1][winner-1] = -1
    
    for i in range(100):
        for irow, row in enumerate(table):
            for icol, col in enumerate(row):
                if col == 1:
                    for icol2, col2 in enumerate(table[icol]):
                        if col2 == 1:
                            table[irow][icol2] = 1
                if col == -1:
                    for icol2, col2 in enumerate(table[icol]):
                        if col2 == -1:
                            table[irow][icol2] = -1

    answer = sum([1 for row in table if sum([1 for col in row if col != 0]) == n-1])
    return answer