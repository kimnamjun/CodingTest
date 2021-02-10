# 정확도 통과

class Node:
    def __init__(self):
        self.edge = list()

    def search(self, num):
        global answer
        if num == len(path) :
            answer +=1
            return
        for inode in self.edge:
            if inode[1] == path[num]:
                nodes[inode[0]].search(num+1)


answer = 0
lst = list()

n = int(input())
for i in range(n-1):
    u, v, c = map(str, input().split())
    lst.append((int(u), int(v), c))
path = input()

nodes = [Node() for _ in range(n+1)]

for u, v, c in lst:
    nodes[u].edge.append((v, c))

for node in nodes[1:]:
    node.search(0)

print(answer)