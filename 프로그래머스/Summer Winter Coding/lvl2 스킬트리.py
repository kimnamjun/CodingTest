def solution(skill, skill_trees):
    answer = len(skill_trees)
    for sk in skill_trees:
        idx = 0
        for s in sk:
            if s == skill[idx]:
                idx += 1
                if idx == len(skill):
                    break
            elif s in skill[idx+1:]:
                answer -= 1
                break
    return answer