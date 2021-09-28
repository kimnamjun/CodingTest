def solution(n):
    import itertools
    answer = list()
    m = n

    for i in range(n):
        answer.append([0]*(i+1))

    cnt = 0
    lvl = 0
    while cnt < n * (n+1) // 2:
        for i in range(m):
            cnt += 1
            answer[i+lvl*2][0+lvl] = cnt
        m -= 1
        for i in range(m):
            cnt += 1
            answer[m+lvl*2][i+1+lvl] = cnt
        m -= 1
        for i in range(m):
            cnt += 1
            answer[n-lvl-i-2][-lvl-1] = cnt
        m -=1
        lvl += 1

    return list(itertools.chain.from_iterable(answer))