from itertools import combinations

def solution(relation):
    row_num = len(relation)
    columns = [i for i in range(len(relation[0]))]
    super_key = list()
    for key_num in range(len(relation[0])):
        for com in combinations(columns, key_num+1):
            data = set()
            for row in relation:
                string = str()
                for c in com:
                    string += row[c] + '-'
                data.add(string)
            if len(data) == row_num:
                super_key.append(com)

    candidate_key = super_key
    for idx1 in range(len(super_key)):
        idx2 = idx1 + 1
        while idx2 < len(candidate_key):
            if set(candidate_key[idx1]).issubset(set(candidate_key[idx2])):
                candidate_key.pop(idx2)
            else:
                idx2 += 1

    return len(candidate_key)