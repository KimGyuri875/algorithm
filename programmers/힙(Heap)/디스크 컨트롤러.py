import heapq
def solution(jobs):
    answer = 0
    heap = []
    jobs.sort()
    s, e = -1, jobs[0][0]
    time = [0,0]
    count = 0
    while count < len(jobs):
        for i in jobs:
            if s < i[0] <= e:
                heapq.heappush(heap, (i[1],i[0]))
        if heap:
            cost, wait = heapq.heappop(heap)
            s = e
            e += cost
            answer += e-wait
            count+=1
        else:
            e += 1
    return answer//len(jobs)
