# 경우의 수가 정해져 있고 시간복잡도가 O(NlogN) 이내이기 때문에 완전탐색으로 문제를 푼다
# 경우의 수를 먼저 list[tuple] 형태로 지정을 해놓고 비교하는 알고리즘을 작성한다. 

x = input()
y = int(x[1])

x = int(ord(x[0])) - int(ord('a')) + 1
answer = 0
# 경우의 수를 배열에 미리 저장하기
step = [(-2,-1), (-1,-2), (-2,1), (-1,2), (1,-2),(2,-1), (2,1),(1,2)]

for i,j in step:
  check_x = x + i
  check_y = y + j
  if check_x >=1 and check_x <=8 and check_y>=1 and check_y <=8:
    answer += 1

print(answer)
