from collections import Counter, defaultdict

def solution(genres, plays):
    genres_count = dict()
    play_list = list()
    for idx, gen in enumerate(genres):
        genres_count[gen] = genres_count.get(gen, 0) + plays[idx]
        play_list.append([genres[idx], plays[idx], idx])
    for song in play_list:
        song[0] = genres_count[song[0]]
    play_list = sorted(play_list, key=lambda x: (-x[0], -x[1], x[2]))

    answer = list()
    two = defaultdict(int)
    for p in play_list:
        if two[genres[p[2]]] < 2:
            two[genres[p[2]]] += 1
            answer.append(p[2])
    return answer