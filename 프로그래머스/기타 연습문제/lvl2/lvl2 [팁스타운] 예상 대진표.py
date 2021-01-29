def solution(n,a,b):
    a, b = a-1, b-1
    answer = 0
    while a != b:
        answer += 1
        a //= 2
        b //= 2
    return answer