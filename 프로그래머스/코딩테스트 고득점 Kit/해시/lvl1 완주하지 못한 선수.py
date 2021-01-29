def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    for i, _ in enumerate(c):
        if c[i] != p[i]:
            return p[i]
    return p[-1]