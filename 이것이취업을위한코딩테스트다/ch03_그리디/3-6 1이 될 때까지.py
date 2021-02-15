# 정답풀이
# 이문제도 내가 생각한 방식으로 풀면 숫자가 커지면 시간 초과가 발생한다. 
# 즉 while문으로 하나씩 증가하는 방식은 시간 초과가 날 위험이 있다.
n, k = map(int, input().split())
result = 0
while True :
  # 1씩 빼기
  target = (n//k) * k
  result += (n-result)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n-1)
print(result)
