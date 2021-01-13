from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
path = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
#출발도시~출발도시는 0
distance[x] = 0

for _ in range(m):
    start, end = map(int, input().split())
    path[start].append(end)

queue = deque([x])
while queue:
    v = queue.popleft()
    for city in path[v]:
        if distance[city] == -1:
            queue.append(city)
            distance[city] = distance[v]+1

#print(distance)
check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
    
    
"""
import sys
from collections import deque
N, M, K, X = map(int, sys.stdin.readline().split())
node=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    node[a].append(b)

dist = [-1 for _ in range(N+1)]
visit = [1 for _ in range(N+1)]
dist[X] = 0
answer = []

deq = deque([X])
while deq:
    cost = deq.popleft()
    for i in node[cost]:
        if dist[i] == -1:
            dist[i] = dist[cost] + 1
            deq.append(i)

for i, value in enumerate(dist):
    if value == K:
        answer.append(i)
if len(answer) == 0:
    print('-1')
else:
    print(answer)
"""
