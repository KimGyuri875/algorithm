# 정답 풀이
# 큰수가 더해지는 횟수를 구하고 빼기로 두번째로 큰 수가 더해지는 횟수가 나온다.
# 반복문 없이 구할 수 있다. 
M, N, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
first = array[n-1] # array[-1]
second = array[n-2]

# first가 계산 되는 횟수
count = int(m / (k+1)) * k
count += m % (k+1)

result = count * first
result += (m - count) * second
answer = 0
for i in range(N):
  if i % k == k-1:
    answer += array[1]
  else :
    answer += array[0] 
  
# 내 푼 풀이는 M의 숫자가 커지면 시간초과가 발생할 수 있다
M, N, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse = TRUE)
answer = 0
for i in range(N):
  if i % k == k-1:
    answer += array[1]
  else :
    answer += array[0] 
  
