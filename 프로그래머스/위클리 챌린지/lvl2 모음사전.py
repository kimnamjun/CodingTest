from itertools import product

def solution(word):
    s = 'AEIOU'

    arr = list()
    for i in range(5):
        for j in product(s, repeat=i+1):
            arr.append(''.join(j))
    arr.sort()

    dic = {val: idx for idx, val in enumerate(arr)}
    return dic[word] + 1