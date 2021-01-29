def solution(num):
    answer = 0
    while num != 1 and answer < 500:
        answer += 1
        num = num * 3 + 1 if num % 2 else num // 2
    return answer if answer < 500 else -1