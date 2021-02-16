from collections import defaultdict

def solution(tickets):
    airports = defaultdict(list)
    for frm, to in tickets:
        airports[frm].append(to)
    for airport in airports:
        airports[airport].sort()

    def dfs(path, tickets_ap):
        if len(path) == len(tickets) + 1:
            return path

        for dest in tickets_ap[path[-1]]:
            tickets_ap[path[-1]].remove(dest)
            ret = dfs(path + [dest], tickets_ap)
            if ret:
                return ret
            tickets_ap[path[-1]].append(dest)
            tickets_ap[path[-1]].sort()

    return dfs(['ICN'], airports)