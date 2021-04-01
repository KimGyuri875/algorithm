N = (int(input()))
num = []
for i in range(N):
    num.append( list(map(int,input().split())))

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            num[i][j]+=num[i-1][j]
        elif j == i:
            num[i][j] += num[i-1][j-1]
        else:
            num[i][j] = max( num[i][j], num[i][j] + num[i-1][j-1], num[i][j] + num[i-1][j] )

print(max(num[-1]))

'''
# 정수 삼각형
# 아래로 내려오면서 합이 최대 약간 연쇄? 느낌이 나네

# 입력 크기n
import sys
input = sys.stdin.readline

n = int(input())
t = [list(map(int , input().split())) for i in range(n)]

# dp 를 위한 메모리 만들기
# 각 높이의 최대? 피라미드 같은 형태를 만들자
dp = [[0] * i for i in range(1,n+1)]
#print(dp)
# for 문을 통해서 업데이트 시켜주자
dp[0][0] = t[0][0]

for i in range(1, n):
    for j in range(0,i+1):
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] +t[i][j])
        elif j == i:
            dp[i][j] = max(dp[i][j], dp[i - 1][j-1] + t[i][j])
        else:
            dp[i][j] = max(dp[i - 1][j] +t[i][j], dp[i - 1][j-1] + t[i][j])
#print(dp)
print(max(dp[-1]))
'''
