def solution(n, computers):
    def union(a, b):
        fa = find(a)
        fb = find(b)
        if fa != fb:
            nodes[fb] = fa

    def find(a):
        if a != nodes[a]:
            nodes[a] = find(nodes[a])
        return nodes[a]

    nodes = [i for i in range(n)]

    for i in range(n):
        for j in range(i):
            if computers[i][j]:
                union(i, j)

    for idx, val in enumerate(nodes):
        nodes[idx] = find(val)
    
    return len(set(nodes))