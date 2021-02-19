# 참고 : https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
from collections import defaultdict

def solution(sales, links):
    def get_d(i):
        sum_child = 0
        for k in nodes[i]:
            sum_child += min(get_d(k))

        d[i] = [sum_child, sales[i] + sum_child]

        if nodes[i]:
            d[i][0] += min(max(0, d[k][1] - d[k][0]) for k in nodes[i])

        return d[i]

    nodes = defaultdict(list)
    for parent, child in links:
        nodes[parent].append(child)

    sales.insert(0, 0)
    d = [list() for _ in range(len(sales) + 1)]
    return min(get_d(1))