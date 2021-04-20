import sys
sys.setrecursionlimit(300000)

def solution(a, edges):
    if sum(a):
        return -1

    nodes = [[i, list(), -1, -1] for i in a]  # weight, linked_nodes, depth, parent
    for n1, n2 in edges:
        nodes[n1][1].append(n2)
        nodes[n2][1].append(n1)

    nodes[0][2] = 0
    stack = [0]
    while stack:
        top = stack.pop()
        for inode in nodes[top][1]:
            if nodes[inode][2] == -1:
                nodes[inode][2] = nodes[top][2] + 1
                nodes[inode][3] = top
                stack.append(inode)

    for idx, (weight, children, depth, parent) in enumerate(nodes):
        if parent != -1:
            nodes[idx][1].remove(parent)

    def calc(inode):
        ret = 0
        for child in nodes[inode][1]:
            ret += calc(child)
        if nodes[inode][3] != -1:
            nodes[nodes[inode][3]][0] += nodes[inode][0]
        ret += abs(nodes[inode][0])
        return ret

    return calc(0)
