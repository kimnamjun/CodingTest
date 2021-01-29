def solution(triangle):
    answer = [triangle[0]]
    for irow, row in enumerate(triangle[1:], start=1):
        data = list()
        for icol, col in enumerate(row):
            if icol == 0:
                data.append(answer[irow-1][0] + col)
            elif icol == len(row) - 1:
                data.append(answer[irow-1][-1] + col)
            else:
                data.append(max(answer[irow-1][icol-1], answer[irow-1][icol]) + col)
        answer.append(data)
    return max(answer[-1])