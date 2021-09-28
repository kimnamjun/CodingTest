from itertools import product

def solution(grid):
    answer = list()
    width, height = len(grid[0]), len(grid)
    dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    sign = {'S': 0, 'R': 1, 'L': 3}
    table = [[[0 for d in range(4)] for x in range(width)] for y in range(height)]
    for x, y, d in product(range(width), range(height), range(4)):
        if table[y][x][d]:
            continue
        n = 0
        while not table[y][x][d]:
            table[y][x][d] = 1
            n += 1
            x = (x + dt[d][0]) % width
            y = (y + dt[d][1]) % height
            d = (d + sign[grid[y][x]]) % 4
        answer.append(n)
    return sorted(answer)