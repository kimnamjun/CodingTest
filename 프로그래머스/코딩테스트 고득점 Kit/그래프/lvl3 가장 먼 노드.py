from collections import defaultdict

def solution(n, edge):
    nodes = [0] + [n] * (n-1)
    link = defaultdict(list)

    for e in edge:
        link[e[0]-1].append(e[1]-1)
        link[e[1]-1].append(e[0]-1)

    stk = [0]
    while stk:
        top = stk[-1]
        stk.pop()
        for i in link[top]:
            if nodes[top] + 1 < nodes[i]:
                nodes[i] = nodes[top] + 1
                stk.append(i)

    maxi = max(nodes)
    answer = 0
    for n in nodes:
        if n == maxi:
            answer += 1
    return answer