def solution(play_time, adv_time, logs):
    play_time2 = int(play_time[:2]) * 3600 + int(play_time[3:5]) * 60 + int(play_time[6:])
    adv_time2 = int(adv_time[:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:])
    logs2 = [[int(log[:2]) * 3600 + int(log[3:5]) * 60 + int(log[6:8]),
              int(log[9:11]) * 3600 + int(log[12:14]) * 60 + int(log[15:])] for log in logs]

    lines_dict = {0: 0, play_time2: 0}
    for left, right in logs2:
        lines_dict[left] = lines_dict.get(left, 0) + 1
        lines_dict[right] = lines_dict.get(right, 0) - 1

    height = 0
    lines_list = sorted(lines_dict.items())
    lines = list()
    for idx in range(len(lines_dict) - 1):
        height += lines_list[idx][1]
        lines.append([lines_list[idx][0], lines_list[idx + 1][0], height])

    check_times = list()
    for left, right, view in lines:
        if left + adv_time2 <= play_time2:
            check_times.append([left, left + adv_time2])
        if right - adv_time2 >= 0:
            check_times.append([right - adv_time2, right])

    def segment_tree_search(start, end, left, right):
        if start >= lines[right][1] or end <= lines[left][0]:
            return 0
        if left == right:
            x1 = min(end, lines[left][1])
            x2 = max(start, lines[left][0])
            x3 = lines[left][2]
            x4 = (x1 - x2) * x3
            return x4
        x1 = segment_tree_search(start, end, left, (left + right) // 2)
        x2 = segment_tree_search(start, end, (left + right) // 2 + 1, right)
        return x1 + x2

    answer_time, answer_score = 0, 0
    for start, end in sorted(check_times):
        score = segment_tree_search(start, end, 0, len(lines) - 1)
        if score > answer_score:
            answer_time = start
            answer_score = score

    return f'{str(answer_time // 3600).zfill(2)}:{str(answer_time % 3600 // 60).zfill(2)}:{str(answer_time % 60).zfill(2)}'