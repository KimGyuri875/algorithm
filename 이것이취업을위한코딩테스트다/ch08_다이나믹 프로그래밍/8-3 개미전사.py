n = int(input())
food = list(map(int, input().split()))
check = [0] * (n + 1)
check[0] = food[0]

#check[1] = food[1]
check[1] = max(food[0], food[1])

for i in range(2, n):
  check[i] = max(check[i-2] + food[i], check[i-1])

print(max(check))
