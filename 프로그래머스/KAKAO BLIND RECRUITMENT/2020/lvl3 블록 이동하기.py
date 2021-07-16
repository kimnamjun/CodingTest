from collections import deque
LARGE_NUMBER = 10000


def solution(board):
    n = len(board)
    horizontal = list()
    vertical = list()
    for row in board:
        for col in row:
            if col:
                horizontal.append(-1)
                vertical.append(-1)
            else:
                horizontal.append(LARGE_NUMBER)
                vertical.append(LARGE_NUMBER)

    horizontal[0] = 0
    queue = deque([[1, 0]])
    while queue:
        sign, pos = queue.popleft()
        if sign:  # horizontal
            cur = horizontal[pos] + 1
            left = pos % n != 0 and horizontal[pos - 1] != -1
            right = pos % n != n - 2 and horizontal[pos + 2] != -1
            up = pos // n != 0 and horizontal[pos - n] != -1 and horizontal[pos - n + 1] != -1
            down = pos // n != n - 1 and horizontal[pos + n] != -1 and horizontal[pos + n + 1] != -1

            if left and cur < horizontal[pos - 1]:  # 왼쪽 이동
                horizontal[pos - 1] = cur
                queue.append([1, pos - 1])
            if right and cur < horizontal[pos + 1]:  # 오른쪽 이동
                horizontal[pos + 1] = cur
                queue.append([1, pos + 1])
            if up:
                if cur < horizontal[pos - n]:  # 위쪽 이동
                    horizontal[pos - n] = cur
                    queue.append([1, pos - n])
                if cur < vertical[pos - n]:  # 왼쪽 축 반시계
                    vertical[pos - n] = cur
                    queue.append([0, pos - n])
                if cur < vertical[pos - n + 1]:  # 오른쪽 축 시계
                    vertical[pos - n + 1] = cur
                    queue.append([0, pos - n + 1])
            if down:
                if cur < horizontal[pos + n]:  # 아래쪽 이동
                    horizontal[pos + n] = cur
                    queue.append([1, pos + n])
                if cur < vertical[pos]:  # 왼쪽 축 시계
                    vertical[pos] = cur
                    queue.append([0, pos])
                if cur < vertical[pos + 1]:  # 오른쪽 축 반시계
                    vertical[pos + 1] = cur
                    queue.append([0, pos + 1])

        else:  # vertical
            cur = vertical[pos] + 1
            left = pos % n != 0 and vertical[pos - 1] != -1 and vertical[pos + n - 1] != -1
            right = pos % n != n - 1 and vertical[pos + 1] != -1 and vertical[pos + n + 1] != -1
            up = pos // n != 0 and vertical[pos - n] != -1
            down = pos // n != n - 2 and vertical[pos + n * 2] != -1

            if up and cur < vertical[pos - n]:  # 위쪽 이동
                vertical[pos - n] = cur
                queue.append([0, pos - n])
            if down and cur < vertical[pos + n]:  # 아래쪽 이동
                vertical[pos + n] = cur
                queue.append([0, pos + n])
            if left:
                if cur < vertical[pos - 1]:  # 왼쪽 이동
                    vertical[pos - 1] = cur
                    queue.append([0, pos - 1])
                if cur < horizontal[pos - 1]:  # 위쪽 축 시계
                    horizontal[pos - 1] = cur
                    queue.append([1, pos - 1])
                if cur < horizontal[pos + n - 1]:  # 아래쪽 축 반시계
                    horizontal[pos + n - 1] = cur
                    queue.append([1, pos + n - 1])
            if right:
                if cur < vertical[pos + 1]:  # 오른쪽 이동
                    vertical[pos + 1] = cur
                    queue.append([0, pos + 1])
                if cur < horizontal[pos]:  # 위쪽 축 반시계
                    horizontal[pos] = cur
                    queue.append([1, pos])
                if cur < horizontal[pos + n]:  # 아래쪽 축 시계
                    horizontal[pos + n] = cur
                    queue.append([1, pos + n])

    answer_h = horizontal[n*n-2] if horizontal[n*n-2] != -1 else LARGE_NUMBER
    answer_v = vertical[n*n-n-1] if vertical[n*n-n-1] != -1 else LARGE_NUMBER
    return min(answer_h, answer_v)
