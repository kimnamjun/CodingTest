def solution(n, lost, reserve):
    i = 0
    while i < len(lost):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost.pop(i)
        else:
            i += 1

    i = 0
    answer = n
    while i < n:
        i += 1
        if i in lost:
            if i-1 in reserve:
                reserve.remove(i-1)
            elif i in reserve:
                reserve.remove(i)
            elif i+1 in reserve:
                reserve.remove(i+1)
            else:
                answer -= 1
    return answer