from collections import deque

def solution(priorities, location):
    sorted_priorities = sorted(priorities)
    arr = deque([(idx, val) for idx, val in enumerate(priorities)])

    answer = 0
    while arr:
        if arr[0][1] != sorted_priorities[-1]:
            arr.append(arr[0])
            arr.popleft()
            continue

        answer += 1
        if arr[0][0] == location:
            return answer
        arr.popleft()
        sorted_priorities.pop()
    return -1