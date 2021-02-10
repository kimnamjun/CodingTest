# 정확성 통과

from math import sqrt, floor

def solution(begin, end):
    answer = list()
    if begin == 1:
        answer = [0]
        begin = 2

    for num in range(begin, end+1):
        x = 1
        for i in range(2, floor(sqrt(num))+1):
            if num % i == 0:
                x = num // i
                break
        answer.append(x)
    return answer