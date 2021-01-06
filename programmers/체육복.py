def solution(n, lost, reserve):
    answer = 0
    cloth = [0 for _ in range(n)]

    # 여벌이 도난 후 몇개인지를 파악
    for i in lost:
        cloth[i-1] -=1
    for i in reserve:
        cloth[i-1] +=1

    #앞에 애가 뒤에 애 빌려준다 
    for i in range(n):
        if cloth[i] == -1:
            if i > 0 and cloth[i-1] == 1:
                cloth[i] +=1
                cloth[i-1] -=1
            elif i < n-1 and cloth[i+1] == 1:
                cloth[i] +=1
                cloth[i+1] -=1
    for i in cloth:
        if i >= 0 :
            answer +=1
    return answer
    
'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]      # 이렇게 간결하게 코드짜는 연습을 해보자!
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''
