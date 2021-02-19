from collections import deque

def solution(n, t, m, timetable):
    answer = 0
    bus = [540 + t * i for i in range(n)]
    timetable = deque(sorted([int(tm[0:2]) * 60 + int(tm[3:5]) for tm in timetable]))
    waiting = deque()

    for b in bus:
        while len(waiting) < m:
            if timetable and timetable[0] <= b:
                waiting.append(timetable.popleft())
            else:
                break

        answer = waiting[-1] - 1 if len(waiting) == m else b

        for i in range(m):
            if waiting:
                waiting.popleft()

    return f'{str(answer // 60).zfill(2)}:{str(answer % 60).zfill(2)}'