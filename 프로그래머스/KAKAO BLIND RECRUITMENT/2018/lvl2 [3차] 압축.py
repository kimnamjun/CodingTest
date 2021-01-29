def solution(msg):
    answer = list()
    dic = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}

    start, end = 0, 0
    while end < len(msg):
        if msg[start:end+1] in dic:
            end += 1
        else:
            answer.append(dic[msg[start:end]])
            dic.update({msg[start:end+1]: len(dic)+1})
            start = end
    answer.append(dic[msg[start:end]])
    return answer