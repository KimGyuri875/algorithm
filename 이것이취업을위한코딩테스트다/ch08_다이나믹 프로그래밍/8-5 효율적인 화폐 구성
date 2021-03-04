# 
n,m = map(int, input().split())
money = []
for _ in range(n):
  money.append(int(input()))

d = [10001] * (m+1)
# 첫번째 값을 0 으로 초기화 해줌으로써 특정 화폐가 있는지를 check 할 수 있다!!
d[0] = 0

for i in range(n):
  for j in range(money[i], m + 1):
    if d[j-money[i]] != 10001:
      d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
  
