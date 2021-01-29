def solution(x):
    y = x
    z = 0
    while y:
        z += y % 10
        y //= 10
    return False if x % z else True