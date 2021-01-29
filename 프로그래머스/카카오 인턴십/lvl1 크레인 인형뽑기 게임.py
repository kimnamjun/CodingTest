def solution(board, moves):
    answer = 0

    lines = list()
    length = len(board)
    for _ in range(length):
        lines.append(list())
    for data in board[::-1]:
        for idx, val in enumerate(data):
            if val:
                lines[idx].append(val)

    basket = list()
    for i in moves:
        if lines[i-1]:
            basket.append(lines[i-1].pop())
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2

    return answer