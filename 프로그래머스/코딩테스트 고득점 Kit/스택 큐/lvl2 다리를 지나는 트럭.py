from collections import deque

def solution(bridge_length,	weight,	truck_weights):
    waiting = deque(truck_weights)
    on_bridge = deque()
    w = 0
    time = 0

    while waiting or on_bridge:
        time = time + 1 if waiting and w + waiting[0] <= weight else bridge_length + on_bridge[0][1]
        
        if on_bridge and time >= bridge_length + on_bridge[0][1]:
            w -= on_bridge[0][0]
            on_bridge.popleft()
            
        if waiting and w + waiting[0] <= weight:
            w += waiting[0]
            on_bridge.append((waiting[0], time))
            waiting.popleft()

    return time