# 쉬운 문제지만 lamdba를 사용하는 좋은 예시 문제이다
# 또 꼭 바로 input 해서 append 할 생각하지 말고 나눠서 하는 시각도 기르자
n = int(input())
array = []
for _ in range(n):
  data = list(input().split())
  array.append([data[0], int(data[1])])
array = sorted(array , key = lambda x : x[1])
for i in array:
  print(i[0], end =" ")
