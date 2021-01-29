from collections import defaultdict, deque

def solution(n, s, a, b, fares):
    large_number = 20000000
    costs = [[large_number, large_number, large_number] for _ in range(n+1)]

    fare_dict = defaultdict(list)
    for c, d, f in fares:
        fare_dict[c].append([d, f])
        fare_dict[d].append([c, f])

    for i in range(3):
        que = deque([[s,0] if i == 0 else [a,0] if i == 1 else [b,0]])
        while que:
            node, fare = que[0]
            que.popleft()
            if costs[node][i] <= fare:
                continue
            costs[node][i] = fare
            for d, f in fare_dict[node]:
                que.append([d, fare + f])

    answer = large_number
    for cost in costs:
        answer = min(answer, sum(cost))

    return answer