def solution(money):
    table1 = [money[0]]
    table2 = [0]
    for idx, val in enumerate(money[1:], start=1):
        a, b = table2[-1] + val, max(table1[-1], table2[-1])
        table1.append(a)
        table2.append(b)
    answer = max(table1[-2], table2[-1])
    
    table1 = [0]
    table2 = [0]
    for idx, val in enumerate(money[1:], start=1):
        a, b = table2[-1] + val, max(table1[-1], table2[-1])
        table1.append(a)
        table2.append(b)
    answer = max(answer, table1[-1], table2[-1])
    
    return answer