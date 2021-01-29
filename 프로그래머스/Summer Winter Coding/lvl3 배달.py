def solution(N, road, K):
    class Node:
        def __init__(self):
            self.dist = float('inf')
            self.roads = list()

        def dfs(self, d):
            if d >= self.dist:
                return
            self.dist = d
            for other, cost in self.roads:
                nodes[other].dfs(self.dist + cost)

    nodes = [Node() for _ in range(N+1)]
    for a, b, c in road:
        nodes[a].roads.append((b, c))
        nodes[b].roads.append((a, c))

    nodes[1].dfs(0)

    return sum(1 for node in nodes if node.dist <= K)