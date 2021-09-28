import sys
sys.setrecursionlimit(300000)


def solution(n, edges):
    class Node:
        def __init__(self, num):
            self.num = num
            self.link = list()
            self.dist = [-1, -1, -1]

        def dfs(self, t, d):
            if self.dist[t] != -1 and self.dist[t] <= d:
                return
            self.dist[t] = d
            for num in self.link:
                nodes[num].dfs(t, d + 1)

    # 노드 생성 및 에지 연결
    nodes = [Node(num) for num in range(n+1)]
    for a, b in edges:
        nodes[a].link.append(b)
        nodes[b].link.append(a)

    # 가장 먼 두 노드 번호
    max_index = [1, 1]

    # 가장 먼 두 노드와 그 노드에서의 거리
    nodes[1].dfs(0, 0)

    max_dist = 0
    for idx, node in enumerate(nodes):
        if node.dist[0] > max_dist:
            max_index[0] = idx
            max_dist = node.dist[0]

    nodes[max_index[0]].dfs(1, 0)

    max_dist = 0
    for idx, node in enumerate(nodes):
        if node.dist[1] > max_dist:
            max_index[1] = idx
            max_dist = node.dist[1]

    nodes[max_index[1]].dfs(2, 0)

    # 가장 먼 두 노드를 제외하고 그 다음으로 먼 값 찾기
    answer = 0
    for idx, node in enumerate(nodes[1:], start=1):
        if idx in max_index:
            continue
        answer = max(answer, node.dist[1], node.dist[2])

    return answer