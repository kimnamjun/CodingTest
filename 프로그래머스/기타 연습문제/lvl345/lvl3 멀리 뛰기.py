def solution(n):
    arr = [0, 1]
    for i in range(n):
        arr.append((arr[-2] + arr[-1])%1234567)
    return arr[-1]