def solution(cookie):
    answer = 0

    table = list()
    for i in range(len(cookie)):
        row = [0] * (i + 1)
        for j in range(i, len(cookie)):
            row.append(row[-1] + cookie[j])
        table.append(row[1:])

    for i in range(len(cookie) - 1):
        a_idx = 0
        b_idx = len(cookie) - 1
        a = table[a_idx][i]
        b = table[i + 1][b_idx]

        while b_idx - a_idx != 0:
            if a > b:
                a_idx += 1
                a = table[a_idx][i]
            elif a < b:
                b_idx -= 1
                b = table[i + 1][b_idx]
            else:
                answer = max(answer, a)
                break

    return answer