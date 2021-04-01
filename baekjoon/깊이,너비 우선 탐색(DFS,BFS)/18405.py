import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque()
data = []
graph = []
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if data[i][j] != 0:
            graph.append((data[i][j], 0, i, j))

S, X, Y = map(int, sys.stdin.readline().split())
graph.sort()
q = deque(graph)
while q:
    value, time, x, y = q.popleft()
    if time == S:
        break
    for i,j in zip(move_x,move_y):
        if 0<=x+i<N and 0<=y+j<N:
            if data[x+i][y+j] == 0:
                data[x+i][y+j] = value
                q.append(( data[x+i][y+j], time+1, x+i, y+j ))

print(data[X-1][Y-1])

'''
# 경쟁적 전염

# N * N 시험관
# 1 ~ k번까지의 바이러스 종류
# 바이러스는 1초마다 상.하,좌,우의 방향으로 증식
# 우선순위 : 숫자가 작은 바이러스
# 한 칸에는 한가지 바이러스만

# (x-1,y-1)에 존재하는 바이러스는?

# heapq 를 쓰려고 했지만 그냥 sort()하는게 나음..
import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
b = [list(map(int, input().split())) for i in range(n)]
s,x,y = map(int, input().split())
h = []
mx = [-1,1,0,0]
my = [0,0,-1,1]
for i in range(n):
    for j in range(n):
        if b[i][j] != 0:
            heapq.heappush(h,(b[i][j],i,j,0))

while h:
    p = heapq.heappop(h)
    if p[3] == s*k:
        continue
    for i, j in zip(mx,my):
        if 0<=p[1]+i<n and 0<=p[2]+j<n:
            if b[p[1]+i][p[2]+j] == 0:
                b[p[1] + i][p[2] + j] = p[0]-p[3]
                heapq.heappush(h, (b[p[1] + i][p[2] + j] + k,p[1]+i, p[2]+j, p[3] + k ))

#print(b)
print(b[x-1][y-1])
'''
