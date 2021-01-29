def solution(board):
    wall = list()
    for x in board:
        wall.extend(x)
    length = len(board)
    v_cost = [float('INF') for _ in range(length * length)]
    h_cost = [float('INF') for _ in range(length * length)]

    v_cost[0] = 0
    h_cost[0] = 0

    que = [0]
    while que:
        num = que[0]
        if num >= length and not wall[num - length]:
            if v_cost[num - length] > v_cost[num] + 100:
                v_cost[num - length] = v_cost[num] + 100
                que.append(num - length)
            elif v_cost[num - length] > h_cost[num] + 600:
                v_cost[num - length] = h_cost[num] + 600
                que.append(num - length)
        if num % length != 0 and not wall[num - 1]:
            if h_cost[num - 1] > h_cost[num] + 100:
                h_cost[num - 1] = h_cost[num] + 100
                que.append(num - 1)
            elif h_cost[num - 1] > v_cost[num] + 600:
                h_cost[num - 1] = v_cost[num] + 600
                que.append(num - 1)
        if num % length != length - 1 and not wall[num + 1]:
            if h_cost[num + 1] > h_cost[num] + 100:
                h_cost[num + 1] = h_cost[num] + 100
                que.append(num + 1)
            elif h_cost[num + 1] > v_cost[num] + 600:
                h_cost[num + 1] = v_cost[num] + 600
                que.append(num + 1)
        if num < length * length - length and not wall[num + length]:
            if v_cost[num + length] > v_cost[num] + 100:
                v_cost[num + length] = v_cost[num] + 100
                que.append(num + length)
            elif v_cost[num + length] > h_cost[num] + 600:
                v_cost[num + length] = h_cost[num] + 600
                que.append(num + length)
        del que[0]

    return min(v_cost[-1], h_cost[-1])