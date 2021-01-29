from itertools import combinations

def solution(orders, course):
    alphabet = set()
    for order in orders:
        alphabet.update(order)
    alphabet = sorted(alphabet)
    
    answer = list()
    for c in course:
        dic = dict()
        for combo in combinations(alphabet, c):
            count = len(orders)
            for order in orders:
                for com in combo:
                    if com not in order:
                        count -= 1
                        break
            dic[''.join(combo)] = count

        maxi = max(dic.values())
        if maxi < 2:
            break
        answer.extend([key for key in dic if dic[key] == maxi])

    return sorted(answer)