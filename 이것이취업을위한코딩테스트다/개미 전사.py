# 개미전사
# 약간 그리디? 느낌으로
# 최소 한칸 이상 떨어진 식량창고를 약탈해야한다.
# 얻을 수 있는 식량의 최대값

import sys
input = sys.stdin.readline

n = int(input())
k = list(map(int, input().split()))

# dp 니깐 저장 공간을 만들자
dp = [0] * n
# dp는 멀리보지말고 지금까지의 순간만 고려하자!
dp[0] = k[0]
dp[1] = max(k[0], k[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + k[i])
print(dp[-1])

