def solution(s):
    answer = str()
    for x in s.split(' '):
        for i, v in enumerate(x):
            answer += v.lower() if i % 2 else v.upper()
        answer += ' '
    return answer[:-1]