def solution(n, stations, w):
    lines = [(station - w, station + w) for station in stations]

    merged_lines = [(0, 0)] if lines[0][0] > 1 else list()
    start = lines[0][0]
    for i in range(len(lines) - 1):
        if lines[i][1] + 1 < lines[i + 1][0]:
            merged_lines.append((start, lines[i][1]))
            start = lines[i + 1][0]
    merged_lines.append((start, lines[-1][1]))
    if merged_lines[-1][1] < n:
        merged_lines.append((n + 1, n + 1))

    answer = 0
    coverage = w * 2 + 1
    for idx in range(len(merged_lines) - 1):
        answer += (merged_lines[idx + 1][0] - merged_lines[idx][1] - 2) // coverage + 1
    return answer