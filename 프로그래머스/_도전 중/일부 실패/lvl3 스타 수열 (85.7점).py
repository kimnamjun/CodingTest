def solution(a):
    table_stress = {n: -1 for n in a}
    table_index = {n: -1 for n in a}
    table_count = {n: 0 for n in a}
    for num in a:
        table_count[num] += 1

    table_stress[a[0]] = 0
    for idx, num in enumerate(a):
        table_stress[num] += table_index[num] - idx + 2
        table_stress[num] = max(table_stress[num], 0)
        if table_stress[num] == 2:
            table_stress[num] = 0
            table_count[num] -= 1
        table_index[num] = idx
    if table_stress[a[-1]] >= 1:
        table_count[a[-1]] -= 1

    return max(table_count.values()) * 2