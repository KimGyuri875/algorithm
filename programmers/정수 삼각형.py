def solution(triangle):
    temp = triangle

    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0 or j == i+1:
                temp[i][j] += temp[i-1][j]
            elif j == i:
                temp[i][j] += temp[i-1][j-1]
            else:
                temp[i][j] += temp[i-1][j] if temp[i-1][j] > temp[i-1][j-1] else temp[i-1][j-1]

    return max(temp[len(triangle)-1])       # `temp[len(triangle)-1]` 대신 `temp[-1]` 을 써주면 간결
