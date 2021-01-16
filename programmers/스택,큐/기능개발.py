from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses=deque(progresses)
    deq = deque()
    count = 0
    idx = 0
    find = []
    while len(find) != len(progresses):
        for i in range(len(progresses)):                # zip을 이용하는 방법도 존재
            progresses[i] += speeds[i]
        
        for i in range(len(progresses)):
            if progresses[i] >= 100 and i not in find:
                deq.append(i)
                find.append(i)
        while idx in deq:
            deq.remove(idx)
            count += 1
            idx +=1
        if count != 0:
            answer.append(count)
            count = 0
        
    return answer
    
    
"""
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:                             #if문 조건에 만족하면 순차적으로 100%되는 거까지 되고 else로 넘어가니깐 효율적!!!
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
"""
