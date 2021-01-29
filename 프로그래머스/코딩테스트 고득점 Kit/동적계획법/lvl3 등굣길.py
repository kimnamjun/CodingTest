def solution(m, n, puddles):
    big_num = 1000000007
    
    nodes = [0] * m * n
    nodes[0] = 1

    puddles = [(y-1) * m + (x-1) for x, y in puddles]

    for i in range(1, m):
        if i not in puddles:
            nodes[i] = nodes[i-1]

    for i in range(m, m * n):
        if i not in puddles:
            if i % m:
                nodes[i] = (nodes[i-m] + nodes[i-1]) % big_num
            else:
                nodes[i] = nodes[i-m] % big_num

    return nodes[-1]