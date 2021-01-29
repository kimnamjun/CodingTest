def task(n, a, b):
    c = 6 - a - b
    return task(n-1, a, c) + [a, b] + task(n-1, c, b) if n != 1 else [a, b]

def solution(n):
    answer = list()

    lst = task(n, 1, 3)
    print(lst)
    for i in range(len(lst)//2):
        answer.append([lst[i*2], lst[i*2+1]])
    return answer