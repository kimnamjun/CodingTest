def solution(n, path, order):
    # 0번 노드 기준으로 depth 구하기
    temp_nodes = [[list(), -1] for _ in range(n)]  # link, depth

    for a, b in path:
        temp_nodes[a][0].append(b)
        temp_nodes[b][0].append(a)

    temp_nodes[0][1] = 0
    stack = [0]
    while stack:
        top = stack.pop()
        for link in temp_nodes[top][0]:
            if temp_nodes[link][1] == -1:
                temp_nodes[link][1] = temp_nodes[top][1] + 1
                stack.append(link)

    # 제약 조건 고려했을 때 방문 가능한 방 개수 구하기 (위상정렬)
    nodes = [[0, list(), False] for _ in range(n)]  # ref, next, visitable
    for inode, node in enumerate(temp_nodes):
        for linked_node in node[0]:
            if node[1] < temp_nodes[linked_node][1]:
                nodes[inode][1].append(linked_node)
                nodes[linked_node][0] += 1
    for pre, nxt in order:
        nodes[pre][1].append(nxt)
        nodes[nxt][0] += 1

    stack = [0]
    while stack:
        top = stack.pop()
        if nodes[top][0] == 0 and not nodes[top][2]:
            nodes[top][2] = True
            for node in nodes[top][1]:
                nodes[node][0] -= 1
                stack.append(node)

    return sum([1 for node in nodes if node[2] == True]) == n
