# 문제를 시간안에 풀었지만 if 문의 반복으로 코드의 길이가 길다는 점이 아쉽다. 
# 책의 해설을 주석으로 달아놨다.

# n을 입력받기
n = int(input())
array = input().split()
x = 0
y = 0

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_type = ['L','R','U','D']
# 2중 FOR문으로 첫번째 for문은 array, 두번째 for문은 move_type을 비교해서 같으면 temp_x,temp_y에 적용
# 두번째 for문에서 벗어나면 공간을 벗어나는지를 check해서 x,y에 적용한다. 

for a in array:
  if a == 'L':
    if x == 0 :
      continue
    else:
      x = x - 1
  if a == 'R':
    if x == n - 1:
      continue
    else :
      x = x+1
  if a == 'U':
    if y == 0:
      continue
    else :
      y = y-1
  if a == 'D':
    if y == n-1:
      continue
    else :
      y = y+1

print(y+1,x+1)
