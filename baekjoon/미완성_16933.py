# 최단 경로 알고리즘
from collections import deque
n, m, k = map(int, input().split())
way = []
for i in range(n):
    way.append(list(map(int, input())))
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]
visit = [[0] * m for _ in range(n)]

visit[0][0] = 1
deq = deque()
deq.append([0,0])
b = 0
count = 1
day = True
while deq:
    x,y = deq.popleft()
    print(x,y)
    if x == n-1 and y == m-1:
        print('count : ', count)
        break
    for i,j in zip(move_x,move_y):
        if i+x < n and i + x > -1 and j+y < m and j + y > -1 and visit[i+x][j+y] == 0:
            if way[i+x][j+y] == 0:
                visit[i + x][j + y] = 1
                deq.append([i+x, j+y])
            # way[i+x][j+y] == 1:
            elif b < k:
                b += 1
                if day:
                    way[i + x][j + y] = 0
                    deq.append([i+x, j+y])
                    visit[i + x][j + y] = 1
                else:
                    way[i + x][j + y] = 0
                    deq.append([i, j])
    day = not day
    count += 1

print(count)
