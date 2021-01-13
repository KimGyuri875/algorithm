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
