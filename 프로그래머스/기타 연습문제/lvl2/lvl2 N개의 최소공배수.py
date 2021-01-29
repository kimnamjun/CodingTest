import math

# solution = lambda x: math.lcm(*arr)  # python 3.9 이상

def solution(arr):
    answer = 1
    for a in arr:
        answer = answer * a // math.gcd(answer, a)
    return answer