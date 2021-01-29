def solution(n, k):
    k -= 1
    table = [i+1 for i in range(n)]
    factorial = [1]
    for i in range(20):
        factorial.append(factorial[-1] * (i+1))

    answer = list()
    for i in range(n-1, -1, -1):
        select = k // factorial[i]
        k %= factorial[i]
        answer.append(table[select])
        table = table[:select] + table[select+1:]
    
    return answer