def is_valid(_answer):
    for x, y, a in _answer:
        if a:
            if not([x, y-1, 0] in _answer or [x+1, y-1, 0] in _answer or [x-1, y, 1] in _answer and [x+1, y, 1] in _answer):
                return False
        else:
            if not(y == 0 or [x, y-1, 0] in _answer or [x-1, y, 1] in _answer or [x, y, 1] in _answer):
                return False
    return True

def solution(n, build_frame):
    answer = list()
    
    for x, y, a, b in build_frame:
        _answer = list(answer)
        if b:
            _answer.append([x, y, a])
        else:
            _answer.remove([x, y, a])
        result = is_valid(_answer)
        if result:
            answer = _answer

    return sorted(answer)