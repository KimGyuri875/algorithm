# 2003 수들의 합2

# N개의 수로 된 수열a
# a[i] ~ a[j]까지의 합 = M 이 되는 경우의 수

# 1. 그냥 탐색 -> 시간초과
# 2. 깊이우선탐색
# 입력
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
deq = deque()
for i in range(n):
    if a[i] == m:
        cnt += 1
    elif a[i] < m:
        deq.append([i, a[i]])
while deq:
    idx, p = deq.popleft()
    if idx + 1 < n:
        if p+a[idx+1] == m:
            #print(idx+1)
            cnt+=1
        elif p + a[idx+1] < m:
            deq.append([idx+1, p+a[idx+1]])

# 출력
print(cnt)

'''
# 두 포인터(1차원 배열에서 두개의 포인터)
# 두포인터 사용 조건: 배열의 원소가 자연수
# end pointer 증가 -> 부분합 증가
# start pointer 증가 -> 부분합 감소
