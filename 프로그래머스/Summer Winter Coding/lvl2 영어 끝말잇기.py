def solution(n, words):
    dic = dict()
    dic[words[0]] = 1
    for idx, word in enumerate(words[1:], start=1):
        if word[0] != words[idx-1][-1] or dic.get(word, 0):
            return [idx % n + 1, idx // n + 1]
        dic[word] = 1
    return [0, 0]