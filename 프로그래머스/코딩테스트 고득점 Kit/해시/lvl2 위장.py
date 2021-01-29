def solution(clothes):
    dic = dict()
    answer = 1
    for _, c in clothes:
        dic[c] = dic.get(c, 1) + 1
    for v in dic.values():
        answer *= v
    return answer - 1