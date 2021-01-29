def solution(arr):
    answer = list()
    prev = -1
    for a in arr:
        if a != prev:
            answer.append(a)
        prev = a
    return answer