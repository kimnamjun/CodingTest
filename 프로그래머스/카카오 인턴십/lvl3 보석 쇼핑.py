def solution(gems):
    num = len(set(gems))
    answer = [1, len(gems)]
    counter = {gems[0]: 1}

    start, end = 1, 1
    while start <= len(gems) and end <= len(gems):
        if len(counter) == num:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            counter[gems[start-1]] -= 1
            if counter[gems[start-1]] == 0:
                counter.pop(gems[start-1])
            start += 1
        else:
            if end == len(gems):
                break
            counter[gems[end]] = counter.get(gems[end], 0) + 1
            end += 1

    return answer