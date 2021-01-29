def solution(n):
    answer = ''
    c = 0
    while True:
        c += 1

        x = (n - 1) % (3 ** c)
        if x < 3 ** (c - 1):
            answer += '1'
        elif x < 3 ** (c - 1) * 2:
            answer += '2'
        else:
            answer += '4'

        n -= 3 ** c
        if n <= 0:
            break

    return answer[::-1]