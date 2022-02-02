from itertools import permutations

def solution(n, weak, dist):
    answer = 9
    cases = [weak[i:] + [n + weak[j] for j in range(i)] for i in range(len(weak))]

    for case in cases:
        for perm in permutations(dist):
            case_temp = case[:]
            for i, d in enumerate(perm):
                rm = case_temp[-1] - d
                for c in case_temp[::-1]:
                    if c >= rm:
                        case_temp.pop()
                    else:
                        break
                if not case_temp:
                    answer = min(answer, i + 1)
                    break

    return answer if answer != 9 else -1

# test case
# print(solution(200, [0, 10, 55, 100, 110, 155], [40, 40, 1, 1]))