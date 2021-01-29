def solution(n, costs):
    answer = 0
    linked = {0}
    costs.sort(key=lambda x: x[2])
    while len(linked) < n:
        for e in costs:
            if e[0] in linked and e[1] not in linked:
                linked.add(e[1])
            elif e[1] in linked and e[0] not in linked:
                linked.add(e[0])
            else:
                continue
            answer += e[2]
            break
    return answer