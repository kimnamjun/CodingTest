from collections import Counter

def solution(str1, str2):
    string1 = [str1[s:s+2].lower() for s in range(len(str1)-1) if str1[s:s+2].isalpha()]
    string2 = [str2[s:s+2].lower() for s in range(len(str2)-1) if str2[s:s+2].isalpha()]

    counter1 = sorted(Counter(string1).items())
    counter2 = sorted(Counter(string2).items())

    intersect, union = 0, 0
    idx1, idx2 = 0, 0
    while idx1 < len(counter1) and idx2 < len(counter2):
        if counter1[idx1][0] == counter2[idx2][0]:
            intersect += min(counter1[idx1][1], counter2[idx2][1])
            union += max(counter1[idx1][1], counter2[idx2][1])
            idx1 += 1
            idx2 += 1
        elif counter1[idx1][0] < counter2[idx2][0]:
            union += counter1[idx1][1]
            idx1 += 1
        elif counter1[idx1][0] > counter2[idx2][0]:
            union += counter2[idx2][1]
            idx2 += 1
    else:
        while idx1 < len(counter1):
            union += counter1[idx1][1]
            idx1 += 1
        while idx2 < len(counter2):
            union += counter2[idx2][1]
            idx2 += 1

    answer = int((intersect / union if union else 1) * 65536)
    return answer