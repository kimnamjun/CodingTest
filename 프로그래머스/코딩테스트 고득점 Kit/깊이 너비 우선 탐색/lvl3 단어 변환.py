from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    # words[-2], words[-1] = begin, target
    if begin in words:
        words.remove(begin)
    if target in words:
        words.remove(target)
    words.extend([begin, target])

    graph = [list() for _ in range(len(words))]
    dist = [50 for _ in range(len(words))]

    for idx1, word1 in enumerate(words):
        for idx2, word2 in enumerate(words[:idx1]):
            diff = 0
            for i in range(len(begin)):
                if word1[i] != word2[i]:
                    diff += 1
            if diff == 1:
                graph[idx1].append(idx2)
                graph[idx2].append(idx1)

    dist[len(words)-2] = 0
    que = deque([len(words)-2])
    while que:
        front = que[0]
        que.popleft()
        for i in graph[front]:
            if dist[front] + 1 < dist[i]:
                dist[i] = dist[front] + 1
                que.append(i)
    
    return dist[-1] if dist[-1] != 50 else 0