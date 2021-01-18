# 시간 : 10분
import sys

N = (int(input()))
stu = []

for i in range(N):
    stu.append(list(sys.stdin.readline().split()))
    # stu.append(input().split())
    for j in range(1,4):
        stu[i][j] = int(stu[i][j]) # 생략가능

stu.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(stu[i][0])
