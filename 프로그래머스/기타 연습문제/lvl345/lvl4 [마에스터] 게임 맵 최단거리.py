from collections import deque

def solution(maps):
    cols = len(maps[0])

    dist = list()
    for row in maps:
        dist.extend((float('inf') if tile else -1 for tile in row))
    dist[0] = 1

    que = deque([0])
    while que:
        front = que.popleft()
        top, bottom = front - cols, front + cols
        left, right = front - 1, front + 1

        if front == len(maps) * cols - 1:
            return dist[-1]

        if front >= cols and dist[front] + 1 < dist[top]:
            dist[top] = dist[front] + 1
            que.append(top)
        if front % cols != 0 and dist[front] + 1 < dist[left]:
            dist[left] = dist[front] + 1
            que.append(left)
        if front % cols != cols - 1 and dist[front] + 1 < dist[right]:
            dist[right] = dist[front] + 1
            que.append(right)
        if front < (len(maps) - 1) * cols and dist[front] + 1 < dist[bottom]:
            dist[bottom] = dist[front] + 1
            que.append(bottom)

    return -1