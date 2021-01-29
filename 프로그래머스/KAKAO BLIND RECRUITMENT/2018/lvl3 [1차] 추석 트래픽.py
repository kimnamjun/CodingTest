def solution(lines):
    times = list()
    for line in lines:
        time = int(line[11:13]) * 1000 * 60 * 60
        time += int(line[14:16]) * 1000 * 60
        time += int(line[17:19]) * 1000
        time += int(line[20:23])
        end = time
        time = round(float(line[24:-1]) * 1000)
        start = end - time + 1
        times.append([start, 1])
        times.append([end + 1000, -1])

    times.sort()
    
    answer = 0
    count = 0
    for time in times:
        count += time[1]
        answer = max(answer, count)

    return answer