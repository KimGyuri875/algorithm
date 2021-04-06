# 19236버 청소년 상어
# [문제]
# 4 * 4 크기의 공간, (x, y)
# 한칸에 한마리(1 <= 번호 <= 16 , 8가지 방향)
# (0,0)에 들어감 먹어 , 먹은 물고기의 방향으로 간다.
# 물고기 이동 :
# 번호가 작은 물고기부터 순서대로 이동한다.
# 물고기는 한 칸을 이동할 수 있고,
# 이동할 수 있는 칸: 빈 칸, 다른 물고기가 있는 칸
# 이동할 수 없는 칸 : 상어가 있음
# 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전시킨다?
# 이동할 수 있는 칸이 없으면 이동을 하지 않는다
# 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동
# 물고기의 이동이 끝나면 상어가 이동
# 상어는 방향에 있는 칸으로 이동, 한번에 여러 개의 칸을 이동할 수 있다
# 이동 중 지나가는 칸에 있는 물고기는 먹지 않는다. 물고기가 없는 칸으로 이동할 수 없다
# 상어가 이동 칸이 없으면 종료
# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값

# [풀이]
# 1. 최댓값을 구하는거니깐 dp + 움직이기 위한 for?
import sys
input = sys.stdin.readline
a = []
b = []
for i in range(4):
  temp = list(map(int, input().split()))
  a.append([temp[0],temp[2],temp[4],temp[6]])
  b.append([temp[1]-1, temp[3]-1, temp[5]-1, temp[7]-1])

dp = [[0] *4 for _ in range(4)]

# 시계 8가지 방향을 위한 list가 필요하다 반시계니깐
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

# (0,0)에서 시작, 그럼 0,0에 있는 물고기 먹기
dp[0][0] = 1
shark =[a[0][0], b[0][0]]
print('shark: ', shark)

# 각 물고기가 순서대로 어디에 위치하고 있는지 index가 물고기 번호
fish = [0] * 17
for i in range(4):
  for j in range(4):
    fish[a[i][j]] = [i,j]

# 16개의 물고기가 먼저 이동해야한다.
for i in range(1, 17):
  xi, yi = fish[i]
  print(fish[i])
  x = xi + dx[b[xi][yi]]
  y = yi + dy[b[xi][yi]]
  if x == 0 and y == 0:
    # 반시계방향으로 회전시키기
    temp = b[xi][yi]+1 if b[xi][yi]!=7 else 0
    flag = True
    while temp != b[xi][yi] and flag:
      x_temp = xi + dx[temp]
      y_temp = yi + dy[temp]
      if 0 <= x_temp < 4 and 0 <= y_temp < 4:
        # 그자리에 있는 물고기랑 자리 바꾸기, 물고기 방향도 바꿔야함
        fish[i], fish[a[x_temp][y_temp]] = [x_temp, y_temp], [xi, yi]
        a[xi][yi], a[x_temp][y_temp] = a[x_temp][y_temp], a[xi][yi]
        b[xi][yi], b[x_temp][y_temp] = b[x_temp][y_temp], b[xi][yi]
        flag = False
  elif 0 <= x < 4 and 0<= y < 4:
    # 그자리에 있는 물고기랑 자리 바꾸기, 물고기 방향도 바꿔야함
    fish[i],fish[a[x][y]] = [x, y], [xi,yi]
    a[xi][yi], a[x][y] = a[x][y], a[xi][yi]
    b[xi][yi], b[x][y] = b[x][y], b[xi][yi]


# 백 트레킹..? : 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시
# 후보를 포기해 정답을 찾악나느 범용적인 알고리즘
# 재귀로 보통 구현, 재귀 함수가 호출되고 조건에 맞지 않으면 종료되고
# 
