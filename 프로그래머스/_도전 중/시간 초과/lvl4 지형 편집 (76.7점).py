# 정확성 통과, 효율성 일부 통과

from collections import Counter
from itertools import chain

def solution(land, P, Q):
    counter = Counter(chain(*land))

    left, right = min(counter), max(counter)
    while left < right:
        mid1 = (left + right) // 2
        mid2 = mid1 + 1

        cost1, cost2 = 0, 0
        for num, cnt in counter.items():
            cost1 += ((mid1 - num) * P if num < mid1 else (num - mid1) * Q) * cnt
            cost2 += ((mid2 - num) * P if num < mid2 else (num - mid2) * Q) * cnt

        if cost1 == cost2:
            return cost1
        elif cost1 < cost2:
            right = mid1
        elif cost1 > cost2:
            left = mid2

    return sum((left - num) * cnt * P if num < left else (num - left) * cnt * Q for num, cnt in counter.items())