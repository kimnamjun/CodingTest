def solution(n):
    big = 1000000007
    arr = [1, 2]
    for i in range(n // 2 - 1):
        arr = [ (arr[0]+arr[1])%big , ((2*arr[0]+3*arr[1])%big) ]
    return sum(arr) % big