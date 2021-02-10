def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    # 첫 번째 뜯기
    table = [0, 0]
    for stk in sticker:
        table[0], table[1] = table[1] + stk, max(table)
    answer = table[1]

    # 첫 번째 안 뜯기
    table = [0, 0]
    for stk in sticker[1:]:
        table[0], table[1] = table[1] + stk, max(table)
    answer = max(answer, max(table))

    return answer