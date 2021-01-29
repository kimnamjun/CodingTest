def solution(dartResult):
    score = -1
    stack = list()
    for s in dartResult:
        if '0' <= s <= '9':
            if score == -1:
                score = int(s)
            else:
                score = score * 10 + int(s)
        elif s in ('S', 'D', 'T'):
            if s == 'D':
                score *= score
            elif s == 'T':
                score *= score * score
            stack.append(score)
            score = -1
        elif s == '*':
            stack[-1] *= 2
            if len(stack) >= 2:
                stack[-2] *= 2
        elif s == '#':
            stack[-1] *= -1
    return sum(stack)