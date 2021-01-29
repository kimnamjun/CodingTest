def solution(number, k):
    stack = list()
    for idx, num in enumerate(number):
        while stack and stack[-1] < num and k:
            stack.pop()
            k -= 1
            if not k:
                break
        stack.append(num)
    answer = ''.join(stack)[:len(number)-k]
    return answer