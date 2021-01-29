def solution(record):
    users = dict()
    log = list()

    for r in record:
        s = r.split()
        if r[0] == 'E':
            users[s[1]] = s[2]
            log.append((1, s[1]))
        elif r[0] == 'L':
            log.append((0, s[1]))
        elif r[0] == 'C':
            users[s[1]] = s[2]

    answer = list()
    for l in log:
        if l[0]:
            answer.append(f'{users[l[1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{users[l[1]]}님이 나갔습니다.')

    return answer