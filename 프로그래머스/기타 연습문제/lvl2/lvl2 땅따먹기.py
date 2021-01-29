def solution(land):
    answer = land[0]
    for row in land[1:]:
        answer = [max(answer[:icol] + answer[icol + 1:]) + col for icol, col in enumerate(row)]
    return max(answer)