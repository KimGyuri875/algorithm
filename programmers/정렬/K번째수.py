def solution(array, commands):
    answer = []
    for n in range(len(commands)):      # for com in commands: 을 사용한다면 
        i = commands[n][0]- 1           #     array[com[0]-1:com[1]])[com[2]-1]) 으로 접근 할 수 있다. 
        j = commands[n][1]
        k = commands[n][2] -1
        a1 = array[i:j] 
        a1.sort()
        answer.append(a1[k])
    return answer
