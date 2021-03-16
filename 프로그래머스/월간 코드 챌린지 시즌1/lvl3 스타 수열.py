from collections import defaultdict

def solution(a):
    table = defaultdict(list)
    for idx, num in enumerate(a):
        table[num].append(idx)

    answer = 0
    for num in table:
        answer_temp = 0
        right_lock_number = -1
        for idx in table[num]:
            if idx > 0 and a[idx] != a[idx-1] and idx - 1 != right_lock_number:
                answer_temp += 2
            elif idx < len(a) - 1 and a[idx] != a[idx+1]:
                answer_temp += 2
                right_lock_number = idx + 1
        answer = max(answer, answer_temp)

    return answer