n = (int(input()))
m = (int(input()))
node = []
temp = []
INF= 100000000
for i in range(n):
    node.append([INF for j in range(n)])

for i in range(m):
    temp = list(map(int, input().split()))
    node[temp[0]-1][temp[1]-1] = min(node[temp[0]-1][temp[1]-1], temp[2])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and node[i][k] + node[k][j] < node [i][j]:
                node[i][j] = node[i][k] + node[k][j]
for i in range(n):
    for j in range(n):
        if node[i][j] == INF:
            print('0', end=" ")
        else:
            print(node[i][j], end=" ")
    print()
