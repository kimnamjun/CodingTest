def solution(N, stages):
    numerator = [0] * (N+2)
    denominator = [0] * (N+2)

    for s in stages:
        numerator[s] += 1

    prev = 0
    for t in range(len(numerator))[::-1]:
        denominator[t] = prev + numerator[t]
        prev = denominator[t]

    fail_rate = list()
    for i, (a, b) in enumerate(zip(numerator, denominator)):
        if b:
            fail_rate.append([i, a / b])
        else:
            fail_rate.append([i, 0])
        
    fail_rate = sorted(fail_rate[1:-1], key=lambda x: (-x[1], x[0]))

    return list(map(lambda x: x[0], fail_rate))