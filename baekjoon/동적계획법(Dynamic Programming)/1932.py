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
