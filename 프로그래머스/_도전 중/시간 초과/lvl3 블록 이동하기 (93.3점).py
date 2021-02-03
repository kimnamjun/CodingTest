import sys
sys.setrecursionlimit(10000)

def solution(board):
    def dfs_h(pos):
        curr1 = horizontal[pos] + 1
        left = pos % n != 0 and horizontal[pos-1] != -1
        right = pos % n != n-2 and horizontal[pos+2] != -1
        up = pos // n != 0 and horizontal[pos-n] != -1 and horizontal[pos-n+1] != -1
        down = pos // n != n-1 and horizontal[pos+n] != -1 and horizontal[pos+n+1] != -1

        if left and curr1 < horizontal[pos-1]:  # 왼쪽 이동
            horizontal[pos-1] = curr1
            dfs_h(pos-1)
        if right and curr1 < horizontal[pos+1]:  # 오른쪽 이동
            horizontal[pos+1] = curr1
            dfs_h(pos+1)
        if up:
            if curr1 < horizontal[pos-n]:  # 위쪽 이동
                horizontal[pos-n] = curr1
                dfs_h(pos-n)
            if curr1 < vertical[pos-n]:  # 왼쪽 축 반시계
                vertical[pos-n] = curr1
                dfs_v(pos-n)
            if curr1 < vertical[pos-n+1]:  # 오른쪽 축 시계
                vertical[pos-n+1] = curr1
                dfs_v(pos-n+1)
        if down:
            if curr1 < horizontal[pos+n]:  # 아래쪽 이동
                horizontal[pos+n] = curr1
                dfs_h(pos+n)
            if curr1 < vertical[pos]:  # 왼쪽 축 시계
                vertical[pos] = curr1
                dfs_v(pos)
            if curr1 < vertical[pos+1]:  # 오른쪽 축 반시계
                vertical[pos+1] = curr1
                dfs_v(pos+1)


    def dfs_v(pos):
        curr1 = vertical[pos] + 1
        left = pos % n != 0 and vertical[pos-1] != -1 and vertical[pos+n-1] != -1
        right = pos % n != n-1 and vertical[pos+1] != -1 and vertical[pos+n+1] != -1
        up = pos // n != 0 and vertical[pos-n] != -1
        down = pos // n != n-2 and vertical[pos+n*2] != -1

        if up and curr1 < vertical[pos-n]:  # 위쪽 이동
            vertical[pos-n] = curr1
            dfs_v(pos-n)
        if down and curr1 < vertical[pos+n]:  # 아래쪽 이동
            vertical[pos+n] = curr1
            dfs_v(pos+n)
        if left:
            if curr1 < vertical[pos-1]:  # 왼쪽 이동
                vertical[pos-1] = curr1
                dfs_v(pos-1)
            if curr1 < horizontal[pos-1]:  # 위쪽 축 시계
                horizontal[pos-1] = curr1
                dfs_h(pos-1)
            if curr1 < horizontal[pos+n-1]:  # 아래쪽 축 반시계
                horizontal[pos+n-1] = curr1
                dfs_h(pos+n-1)
        if right:
            if curr1 < vertical[pos+1]:  # 오른쪽 이동
                vertical[pos+1] = curr1
                dfs_v(pos+1)
            if curr1 < horizontal[pos]:  # 위쪽 축 반시계
                horizontal[pos] = curr1
                dfs_h(pos)
            if curr1 < horizontal[pos+n]:  # 아래쪽 축 시계
                horizontal[pos+n] = curr1
                dfs_h(pos+n)

    n = len(board)
    horizontal = list()
    vertical = list()
    for row in board:
        for col in row:
            if col:
                horizontal.append(-1)
                vertical.append(-1)
            else:
                horizontal.append(10000)
                vertical.append(10000)

    horizontal[0] = 0
    dfs_h(0)

    answer_h = horizontal[n*n-2] if horizontal[n*n-2] != -1 else 10000
    answer_v = vertical[n*n-n-1] if vertical[n*n-n-1] != -1 else 10000
    return min(answer_h, answer_v)