def solution(n):
    answer = 0
    numbers = [i for i in range(n + 1)]
    numbers[0], numbers[1] = 0, 0

    for number in numbers:
        if number == 0:
            continue
        answer += 1
        for num in numbers[::number]:
            numbers[num] = 0
    return answer