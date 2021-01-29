def solution(dirs):
    posi = [5, 5]
    horizon_road = [list([0] * 11) for _ in range(11)]
    vertical_road = [list([0] * 11) for _ in range(11)]

    for dir in dirs:
        if dir == 'L':
            if posi[0] == 0:
                continue
            posi[0] -= 1
            horizon_road[posi[0]][posi[1]] = 1
        elif dir == 'R':
            if posi[0] == 10:
                continue
            horizon_road[posi[0]][posi[1]] = 1
            posi[0] += 1
        elif dir == 'U':
            if posi[1] == 0:
                continue
            posi[1] -= 1
            vertical_road[posi[0]][posi[1]] = 1
        elif dir == 'D':
            if posi[1] == 10:
                continue
            vertical_road[posi[0]][posi[1]] = 1
            posi[1] += 1

    return sum(sum(v) for v in vertical_road) + sum(sum(h) for h in horizon_road)