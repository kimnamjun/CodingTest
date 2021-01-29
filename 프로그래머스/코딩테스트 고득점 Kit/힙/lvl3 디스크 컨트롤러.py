def solution(jobs):
    answer = 0
    length = len(jobs)
    jobque = list()
    jobs.sort()
    time = jobs[0][0]

    while jobs or jobque:
        if not jobque and jobs and jobs[0][0] > time:
            time = jobs[0][0]

        while jobs:
            if jobs[0][0] <= time:
                jobque.append(jobs.pop(0))
            else:
                break
        jobque.sort(key=lambda x: x[1])

        cur = jobque.pop(0)
        time += cur[1]
        answer += time - cur[0]

    return answer // length