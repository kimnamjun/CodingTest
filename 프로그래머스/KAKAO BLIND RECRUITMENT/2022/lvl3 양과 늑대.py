from itertools import permutations

sheep, wolf, wolves = 0, 0, list()

def solution(info, edges):
    global sheep, wolf, wolves

    nodes = [[i, -1, list(), 1] for i in info]  # type, parent, children, check

    for p, c in edges:
        nodes[p][2].append(c)
        nodes[c][1] = p

    # 필요없는 늑대 최대한 버리기
    loop = 1
    while loop:
        loop = 0
        for inode, node in enumerate(nodes):
            if node[0] == 1 and not node[2]:
                nodes[inode][0] = -1
                nodes[nodes[inode][1]][2].remove(inode)
                loop = 1
    wolf_switch = [inode for inode, node in enumerate(nodes) if node[0] == 1]

    # func begin
    def dfs(inode):
        global sheep, wolf, wolves

        if nodes[inode][0] == 0:
            if nodes[inode][3]:
                sheep += 1
                nodes[inode][3] = 0
        elif nodes[inode][0] == 1 and inode in wolves:
            if not nodes[inode][3]:
                pass
            elif nodes[inode][3] and wolf + 1 < sheep:
                wolf += 1
                nodes[inode][3] = 0
            else:
                return
        else:
            return

        for child in nodes[inode][2]:
            dfs(child)
    # func end

    answer = 0
    for perm in permutations(wolf_switch):
        sheep, wolf = 0, 0
        for inode in range(len(nodes)):
            nodes[inode][3] = 1

        for step in range(len(perm)+1):
            wolves = perm[:step]
            dfs(0)
            answer = max(answer, sheep)

    return answer