# 시간이 많이 걸렸지만 완주 성공 
# 오래걸린 이유: tempX, tempY 내용을 써야 하는데 x,y 변수를 써줌 꼼꼼하게 쓰자.
# 정교를 해보자

n,m = map(int, input().split())
data = []
for _ in range(n):
  data.append(list(map(int, input())))

dirX = [-1,1,0,0]
dirY = [0,0,-1,1]
s = [[0,0]]

dist = 2
while s:
  x,y = s.pop()
  dist = data[x][y] + 1
  for i in range(4):
    flag = True
    tempX = dirX[i] + x
    tempY = dirY[i] + y
    if tempX < 0 or tempY < 0 or tempX >= n or tempY >= m:
      # 이런거 대신 continue 써줘도 된다
      flag = False
    elif data[tempX][tempY] == 0:
      flag = False
    elif data[tempX][tempY] == 1 or data[tempX][tempY] > dist:
      # 보다 큰 경우는 비교 안해줘도 된다
      # data[tempX][tempY] == 1 만 확인해 주면 된다. 
      data[tempX][tempY] = dist
      s.append([tempX, tempY])

        
print(data[n-1][m-1])

