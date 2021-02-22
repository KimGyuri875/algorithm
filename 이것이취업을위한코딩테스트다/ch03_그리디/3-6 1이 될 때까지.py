# 정답풀이
# 이문제도 내가 생각한 방식으로 풀면 숫자가 커지면 시간 초과가 발생한다. 
# 즉 while문으로 하나씩 증가하는 방식은 시간 초과가 날 위험이 있다.
n, k = map(int, input().split())
result = 0
while True :
  # 나눠서 나머지가 없는 값으로 target을 만든다. 
  # n // k를 통해서 몫을 구하고 k를 곱하면 나눠어 떨어지는 값이 된다
  # target은 그냥 temp 변수
  target = (n//k) * k
  # 나머지값을 result에 넣기
  result += (n-target)
  n = target
  # n이 k보다 작을 때(즉, 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  result += 1
  n //= k

result += (n-1)
print(result)
