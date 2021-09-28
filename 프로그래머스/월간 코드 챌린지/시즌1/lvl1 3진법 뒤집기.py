def solution(n):
    n3 = str()
    while n:
        n3 += str(n % 3)
        n //= 3
    answer = 0
    for i, s in enumerate(n3[::-1]):
        answer += 3 ** i * int(s)
    return answer