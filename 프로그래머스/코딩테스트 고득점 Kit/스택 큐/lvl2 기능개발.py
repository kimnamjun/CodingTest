import math

def solution(progresses, speeds):
    answer = list()
    days = [math.ceil((100 - val) / speeds[idx]) for idx, val in enumerate(progresses)]
    
    idx = 0
    while idx < len(days):    
        a = 1
        b = days[idx]
        idx += 1
        while idx < len(days) and days[idx] <= b:
            a += 1
            idx += 1
        answer.append(a)
    return answer