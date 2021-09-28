from collections import defaultdict

def solution(id_list, report, k):
    report_id = defaultdict(set)
    report_count = defaultdict(int)

    for r in report:
        a, b = r.split()
        if b not in report_id[a]:
            report_id[a].add(b)
            report_count[b] += 1

    answer = list()
    suspended_id = [user_id for user_id in report_count if report_count[user_id] >= k]
    for user_id in id_list:
        count = 0
        for suspended_user_id in suspended_id:
            if suspended_user_id in report_id[user_id]:
                count += 1
        answer.append(count)
    return answer


# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))