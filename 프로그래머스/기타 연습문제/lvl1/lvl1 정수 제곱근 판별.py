from math import sqrt

def solution(n):
    x = round(sqrt(n))
    if x * x == n:
        return (x+1) * (x+1)
    return -1