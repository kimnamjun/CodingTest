def solution(N, number):
    table = [{int(str(N)*(i+1))} for i in range(8)]
    for i in range(8):
        for j in range((i+1)//2):
            for a in table[j]:
                for b in table[i-j-1]:
                    table[i].add(a + b)
                    table[i].add(a - b)
                    table[i].add(b - a)
                    table[i].add(a * b)
                    if b:
                        table[i].add(a // b)
                    if a:
                        table[i].add(b // a)
        if number in table[i]:
            return i + 1
    return -1