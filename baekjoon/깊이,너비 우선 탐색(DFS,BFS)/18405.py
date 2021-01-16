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
