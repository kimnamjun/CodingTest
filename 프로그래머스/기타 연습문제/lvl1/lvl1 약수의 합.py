def solution(n):
    answer = 0
    for i in range(n):
        if not n % (i+1):
            answer += i+1
    return answer