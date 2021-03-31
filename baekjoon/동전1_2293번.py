# 2293번 동전1

# n가지 종류의 동전 = k 합 의 경우의 수
# 순서만 다른 것은 같은 경우

# 1차 시도 : stack? 형태 -> 메모리 초과

# 2차 시도 : 나누기로
# 나누어서 나머지가 list 안에 있으면 그거 여러가지로 구성
'''
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
deq = deque()
answer = []
cnt = 0
for i in coin:
    q = k // i - 1
    while q>0:
        r = k - (q * i)
        for j in coin:
            if i == j:
                continue
            if r % j == 0:
                print(i, q, j, r // j)
                cnt+=1
        q -= 1

print(cnt)
'''
# dp 문제래,,, 
