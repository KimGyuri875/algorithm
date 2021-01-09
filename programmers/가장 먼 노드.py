from collections import defaultdict
from collections import deque
def solution(n, edge):
    visit = [0 for _ in range(n+1)]
    dist = defaultdict(list)
    count = 1

    for i,j in edge:
        dist[i].append(j)
        dist[j].append(i)

    p = deque(dist[1])
    visit[1]= -1 
    while p:
        for i in range(len(p)):
            v = p.popleft()
            if visit[v] == 0:
                visit[v] = count
                for u in dist[v]: 
                    p.append(u) 
        count +=1

    return visit.count(max(visit))
    
    """
    # 딕셔너리없이 list으로 푸는 방법
        while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1
    for문을 또 안써도 된다는 점에서 효율적인 것 같다. 
    """
    
