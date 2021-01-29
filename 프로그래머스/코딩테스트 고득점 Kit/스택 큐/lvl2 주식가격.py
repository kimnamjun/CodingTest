def solution(prices):
    length = len(prices)
    answer = [0] * length
    stack = list()

    for time, price in enumerate(prices):
        while stack and price < stack[-1][1]:
            answer[stack[-1][0]] = time - stack[-1][0]
            stack.pop()
        stack.append((time, price))

    for stk in stack:
        answer[stk[0]] = length - stk[0] - 1

    return answer