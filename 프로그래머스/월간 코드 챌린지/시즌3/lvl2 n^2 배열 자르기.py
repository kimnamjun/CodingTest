from itertools import chain

def solution(n, left, right):
    row_left, row_right = left // n, right // n
    arr = [[i+1 for _ in range(i+1)] + [i+j+2 for j in range(n-i-1)] for i in range(row_left, row_right + 1)]
    return list(chain.from_iterable(arr))[left-row_left*n:right-row_left*n+1]