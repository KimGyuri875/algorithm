"""
# 정확도 10에서 시간초과가 발생, 스택으로 이용해야하는 이유이다. 근데 왜ㅠㅠ? 종료 조건을 확실히? 
def solution(number, k):
    answer = ''
    count = 0
    i = 0
    number = list(map(int, number))
    
    n = len(number)
    while count < k and i+1 != len(number):
        if i < 0 :
            break
        if number[i] < number[i+1]:
            del number[i]
            count+=1
            i-=1
        else:
            i+=1
            
    answer = "".join(map(str,number))
    answer = answer[:n-k]
    return answer
"""
    
