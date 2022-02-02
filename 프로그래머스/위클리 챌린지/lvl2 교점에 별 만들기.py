from itertools import combinations

def solution(line):
    coordinates = list()
    for (a1, b1, c1), (a2, b2, c2) in combinations(line, 2):
        x_numerator = b1 * c2 - c1 * b2
        y_numerator = a2 * c1 - a1 * c2
        denominator = a1 * b2 - a2 * b1
        if denominator and x_numerator % denominator == 0 and y_numerator % denominator == 0:
            coordinates.append([x_numerator // denominator, y_numerator // denominator])

    min_x, max_x = min(map(lambda z: z[0], coordinates)), max(map(lambda z: z[0], coordinates))
    min_y, max_y = min(map(lambda z: z[1], coordinates)), max(map(lambda z: z[1], coordinates))
    coordinates = list(map(lambda z: [z[0] - min_x, z[1] - min_y], coordinates))
    answer = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for x, y in coordinates:
        answer[-y-1][x] = '*'
    return list(map(lambda z: ''.join(z), answer))