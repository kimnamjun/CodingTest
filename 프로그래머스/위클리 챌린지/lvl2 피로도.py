from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for order in permutations(dungeons):
        fatigue = k
        for clear, (require, consume) in enumerate(order):
            if fatigue < require:
                answer = max(answer, clear)
                break
            fatigue -= consume
        else:
            return clear + 1
    return answer