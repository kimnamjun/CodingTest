def solution(sizes):
    x, y = 0, 0
    for s in map(sorted, sizes):
        x, y = max(x, s[0]), max(y, s[1])
    return x * y