def solution(lottos, win_nums):
    zero, hit = 0, 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
            hit += 1
    best = min(7 - hit - zero, 6)
    worst = min(7 - hit, 6)
    return[best, worst]