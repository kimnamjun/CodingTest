def solution(seoul):
    for i, s in enumerate(seoul):
        if s == 'Kim':
            return f'김서방은 {i}에 있다'