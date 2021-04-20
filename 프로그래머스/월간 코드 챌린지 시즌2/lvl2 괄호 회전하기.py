def is_valid(string):
    stack = list()
    for s in string:
        if s in ('({['):
            stack.append(s)
        elif s in (')}]'):
            if not stack:
                return 0
            elif s == ')' and stack[-1] != '(':
                return 0
            elif s == '}' and stack[-1] != '{':
                return 0
            elif s == ']' and stack[-1] != '[':
                return 0
            else:
                stack.pop()
    return 0 if stack else 1


def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s)
        s = s[1:] + s[0]
    return answer
