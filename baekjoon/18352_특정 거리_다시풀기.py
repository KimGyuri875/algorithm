# 특정 거리의 도시 찾기
# 1 ~ n번까지의 도시, M개의 단방향 도로
# X에서 최단 거리가 K 인 모든 도시
# 메모리 
import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int ,input().split())
d = [list(map(int, input().split())) for i in range(m)]
dist = [[-1] * n for _ in range(n)]
# 최단경로를 구하고 거리가 k인 도시 count
deq = deque()
for i,j in d:
    dist[i-1][j-1] = 1

for i in range(0,1):
    for j in range(n):
        for h in range(n):
            if dist[i][h] != -1 and dist[h][j] != -1:
                if dist[i][j] == -1:
                    dist[i][j] = dist[i][h] + dist[h][j]
                else:
                    dist[i][j] = min(dist[i][j], dist[i][h] + dist[h][j])

cnt = 0
answer = []
#print(dist)
for idx, i in enumerate(dist[x-1]):
    if i == k:
        answer.append(idx+1)
answer.sort()

if len(answer):
    for i in answer:
        print(i)
else:
    print('-1')
