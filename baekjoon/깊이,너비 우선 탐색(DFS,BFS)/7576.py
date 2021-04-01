import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomato = []
deq = deque()
check = [-1,1]
for i in range(0, N):
    tomato.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            deq.append([i, j, 1])
while deq:
    x, y, day = deq.popleft()
    day += 1
    for idx in check:
        if x + idx >= 0 and x + idx < N :
            if tomato[x + idx][y] == 0 and tomato[x+idx][y] != -1:
                tomato[x+idx][y] = day
                deq.append([x+idx, y, day])
        if y + idx >= 0 and y + idx < M and tomato[x][y+idx] != -1:
            if tomato[x][y+idx] == 0:
                tomato[x][y + idx] = day
                deq.append([x, y+idx, day])

flag = False
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            flag = True
            break
    if flag:
        break
if flag:
    print('-1')
else:
    print(max(map(max, tomato))-1)                                # -1 을 해준 이유는 day1과 이미익은 토마토인 '1'과차이를 주기 위해서 day2부터 계

    
# 토마토
# 안익은 토마토의 인접 토마토가 익었으면 익는다
# 최소 일수
# 더 깔끔한 
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
deq = deque()
mx = [-1,1,0,0]
my = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        if t[i][j] == 1:
            deq.append([i, j, 0])

while deq:
    x, y, time = deq.pop()
    for i, j in zip(mx, my):
        if 0<=i+x<n and 0<=j+y<m:
            if t[i+x][j+y] == 0:
                t[i+x][j+y] = 1
                deq.appendleft([i+x, j+y, time+1])

for i in t:
    for j in i:
        if j == 0:
            print('-1')
            sys.exit()
print(time)
