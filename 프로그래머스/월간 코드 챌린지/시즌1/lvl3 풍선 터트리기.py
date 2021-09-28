def solution(a):
    if len(a) <= 2:
        return len(a)

    answer = 2
    left = a[0]

    lst = list()
    right = a[-1]
    for i in a[::-1]:
        right = min(right, i)
        lst.append(right)
    lst = list(reversed(lst))

    for idx, val in enumerate(a[1:-1], start=1):
        if val <= left or val <= right:
            answer += 1
        left = min(left, a[idx])
        right = lst[idx+1]

    return answer