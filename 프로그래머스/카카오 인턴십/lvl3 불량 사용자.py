from itertools import product

# user_id와 banned_id가 서로 매치되는지
def is_matched(uid, bid):
    if len(uid) != len(bid):
        return False
    for i, s in enumerate(bid):
        if s != '*' and s != uid[i]:
            return False
    return True

def solution(user_id, banned_id):
    ban_length = len(banned_id)
    
    # 각 banned_id가 매핑될 수 있는 user_id 번호
    ban = [list() for _ in range(ban_length)]
    for bi, b in enumerate(banned_id):
        for ui, u in enumerate(user_id):
            if is_matched(u, b):
                ban[bi].append(ui)

    # ban에서 중복되지 않게 선택하는 방법
    answer = set()
    for case in product(*ban):
        if len(set(case)) == ban_length:
            answer.add(''.join(map(str, set(case))))
            
    return len(answer)