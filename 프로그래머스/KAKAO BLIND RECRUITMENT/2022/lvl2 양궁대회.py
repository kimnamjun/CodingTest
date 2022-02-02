from collections import Counter
from itertools import combinations_with_replacement

def compare(arr_a, arr_b):
    if arr_a[0] == -1:
        return arr_b
    for a, b in zip(arr_a[::-1], arr_b[::-1]):
        if a > b:
            return arr_a
        elif a < b:
            return arr_b

def solution(n, info):
    answer_diff = 0
    answer = [-1]
    for com in combinations_with_replacement(range(11), n):
        info_ryan = [0 for _ in range(11)]
        for key, value in Counter(com).items():
            info_ryan[key] = value

        ryan, apeach = 0, 0
        for i in range(11):
            if info[i] + info_ryan[i] == 0:
                continue
            elif info[i] >= info_ryan[i]:
                apeach += 10 - i
            else:
                ryan += 10 - i

        diff = ryan - apeach
        if diff > answer_diff or diff == answer_diff and compare(answer, info_ryan) == info_ryan:
            answer_diff = ryan - apeach
            answer = info_ryan

    return answer if answer_diff != 0 else [-1]