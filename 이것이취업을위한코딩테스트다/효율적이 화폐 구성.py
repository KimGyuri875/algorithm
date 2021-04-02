# 효율적이 화폐 구성
# N가지 종류의 화폐
# 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
c = [int(input()) for _ in range(n)]

#dp 를 위한 공간을 만들자
dp= [10001] * (m+1)

for i in c:
    for j in range(i,n + 1):
        dp[j] = min(dp[j], dp[j-i] + 1)
        # 왜 dp[j - i]? j - i?

