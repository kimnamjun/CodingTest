from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = list()

    table = defaultdict(list)
    for data in info:
        s_data = data.split()
        key, score = tuple(s_data[:4]), int(s_data[4])
        for it in range(5):
            for com in combinations(range(4), it):
                key = s_data[:4]
                for co in com:
                    key[co] = '-'
                key = tuple(key)
                table[key].append(score)

    for key in table:
        table[key].sort()

    for qry in query:
        a, b, c, x = qry.split(' and ')
        d, y = x.split()
        target = int(y)
        key = (a, b, c, d)

        if key not in table:
            answer.append(0)
            continue

        left, right = 0, len(table[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if table[key][mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        answer.append(len(table[key]) - left)

    return answer