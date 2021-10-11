def solution(n, wires):
    def set_depth(inode, depth, parent):
        if nodes[inode][0] != -1:
            return
        nodes[inode][0] = depth
        nodes[inode][1] = parent
        nodes[inode][2].remove(parent)
        for child in nodes[inode][2]:
            set_depth(child, depth + 1, inode)

    def set_nodes_num(inode):
        for child in nodes[inode][2]:
            set_nodes_num(child)
            nodes[inode][3] += nodes[child][3]

    nodes = [[-1, 0, list(), 2] for _ in range(n+1)]  # depth, parent, children, node_num * 2

    nodes[1][2] = [0]  # get_depth 떄문에 임시로
    for v1, v2 in wires:
        nodes[v1][2].append(v2)
        nodes[v2][2].append(v1)

    set_depth(1, 0, 0)
    set_nodes_num(1)

    answer = min(abs(node[3] - n) for node in nodes)
    return answer