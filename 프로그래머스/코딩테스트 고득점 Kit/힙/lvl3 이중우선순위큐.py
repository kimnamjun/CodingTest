def solution(operations):
    lst = list()
    for s in operations:
        if s == 'D 1':
            if lst:
                lst.pop()
        elif s == 'D -1':
            if lst:
                lst.pop(0)
        else:
            _, i = s.split()
            lst.append(int(i))
            lst.sort()

    return [max(lst), min(lst)] if lst else [0, 0]