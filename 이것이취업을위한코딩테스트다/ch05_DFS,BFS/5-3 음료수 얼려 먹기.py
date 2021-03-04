# DFS로 푸는 문제
# 재귀로 푼다 
# 
n , m = map(int, input().split())
data = []
for _ in range(n):
  data.append(list(map(int, input())))

def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y>=m:
    return False
  if data[x][y] == 0:
    data[x][y] = 1
    dfs(x, y+1)
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y-1)
    return True
  return False

flag = 0
for i in range(n):
  for j in range(m):
      if dfs(i, j) == True:
        flag+=1
      

print("result",flag)
