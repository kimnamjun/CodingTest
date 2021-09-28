def solution(scores):
    n = len(scores)

    tp = list()  # transpose
    for i in range(n):
        tp.append(list())
        for j in range(n):
            tp[i].append(scores[j][i])

    answer = str()
    for i in range(n):
        tp[i][0], tp[i][i] = tp[i][i], tp[i][0]
        avg_score = sum(tp[i]) / n if min(tp[i][1:]) <= tp[i][0] <= max(tp[i][1:]) else sum(tp[i][1:]) / (n - 1)

        if avg_score < 50:
            answer += 'F'
        elif avg_score < 70:
            answer += 'D'
        elif avg_score < 80:
            answer += 'C'
        elif avg_score < 90:
            answer += 'B'
        else:
            answer += 'A'

    return answer