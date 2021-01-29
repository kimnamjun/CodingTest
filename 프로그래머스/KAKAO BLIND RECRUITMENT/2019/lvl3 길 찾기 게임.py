def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10000)
    
    class Node:
        def __init__(self, index, x, y):
            self.index = index
            self.x = x
            self.y = y
            self.left = None
            self.right = None

        def insert(self, i, x):
            if x < self.x:
                if self.left:
                    self.left.insert(i, x)
                else:
                    self.left = nodes[i]
            else:
                if self.right:
                    self.right.insert(i, x)
                else:
                    self.right = nodes[i]

        def preorder(self):
            pre.append(self.index)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

        def postorder(self):
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            post.append(self.index)

    nodes = list()
    for i, (x, y) in enumerate(nodeinfo):
        nodes.append(Node(i+1, x, y))

    nodes.sort(key=lambda node:(-node.y, node.x))

    for idx, node in enumerate(nodes[1:], start=1):
        nodes[0].insert(idx, node.x)

    pre = list()
    nodes[0].preorder()

    post = list()
    nodes[0].postorder()

    return [pre, post]