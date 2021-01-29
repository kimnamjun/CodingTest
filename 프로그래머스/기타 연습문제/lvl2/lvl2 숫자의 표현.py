def solution(n):
    answer, start = 0, 0
    for i in range(n):
        start += i + 1
        answer += range(start, n+1, i+1).count(n)
    return answer