def solution(answers):
    n = list()
    n.append((len(answers)//5+1)*[1,2,3,4,5])
    n.append((len(answers)//8+1)*[2,1,2,3,2,4,2,5])
    n.append((len(answers)//10+1)*[3,3,1,1,2,2,4,4,5,5])

    a = [0] * 3
    for idx, answer in enumerate(answers):
        for i in range(3):
            if n[i][idx] == answer:
                a[i] += 1

    return [i+1 for i, v in enumerate(a) if v == max(a)]