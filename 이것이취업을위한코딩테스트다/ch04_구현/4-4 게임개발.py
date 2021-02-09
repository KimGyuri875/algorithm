# 
# 문제를 이해하고 요구하는 내용을 오류 없이 성실하게 구현
# 요구 사항을 꼼꼼히!
# 요구 사항의 흐름을 정확히 파악하고 알고리즘 작성하기 (처음엔 BPS 문제로 파악ㅠㅠ)
# 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다. 
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
d[x][y] = 1
count = 1
turn_check = 0
array = []
for i in range(n):
  array.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def turn_left():
  global direction 
  direction -= 1
  if direction == -1:
    direction = 3
while True:
  turn_left()
  # 육지일 경우 & 가본적 없는 땅 
  nx = x + dx[direction]
  ny = y + dy[direction]

  if array[nx][ny] == 0 and d[nx][ny] == 0:
    d[nx][ny] = 1
    count += 1
    turn_check = 0
    x = nx
    y = ny
    continue
  else:
    # 정면이 막히거나 이미 가본칸이다.
    turn_check += 1
  if turn_check == 4:
    # 4방향 다 막혀있다
    # 한칸 뒤로간다
    # 바라보는 방향은 유지한다는게 direction은 변하지 않고
    # 왜 스택으로 안했을까? 뒤로 간다는게 안가본곳을 가는게 아니라(이전으로 돌아가는게 아니라) 바라보는 방향에서 뒤로 향하는거라서 BPS/DFS랑 다른 알고리즘으로 푼다. 
    nx = x - dx[direction]
    ny = y - dy[direction]
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      # 뒤에가 바다 
      break
    # 뒤로 back했으니깐 
    turn_check = 0
print(count)
