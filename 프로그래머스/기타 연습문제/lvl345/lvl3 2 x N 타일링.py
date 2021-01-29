def solution(n):
    a, b = 0, 1
    c = 1000000007
    for i in range(n):
        a, b = b % c, (a + b) % c
    return b