def solution(left, right):
    sq = [i ** 2 for i in range(32)]

    answer = 0
    for i in range(left, right + 1):
        if i in sq:
            answer -= i
        else:
            answer += i
    return answer