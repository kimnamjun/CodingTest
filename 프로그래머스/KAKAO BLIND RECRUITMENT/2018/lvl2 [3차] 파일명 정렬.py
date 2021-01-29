import re

def solution(files):
    num = re.compile(r'\d+')

    answer = list()
    for idx, file in enumerate(files):
        head = re.split(num, file, 1)[0]
        number = re.findall(num, file)[0]
        answer.append((head.lower(), int(number), idx, file))
    
    return [a[3] for a in sorted(answer)]