def solution(s):
    st = list(eval(s[1:-1]))
    if len(st) == 1:
        return st
    st.sort(key=lambda x: len(x))
    answer = [list(st[0])[0]]
    for i in range(len(st)-1):
        answer.extend(st[i+1] - st[i])
    return answer