def solution(number, k):
    answer = ''
    new = []
    for i, num in enumerate(number):
        # stack이 비어있지 않고, 가장 최신거랑 비교했을 때보다 크고, 아직 뺄 수가 남았을 때 
        while len(new) > 0 and new[-1] < num and k > 0:
            new.pop()
            k-=1
        if k == 0:
            new.append(number[i:])
            break
        new.append(num)
    if k != 0:
        new = new[:-k]
    answer = "".join(map(str, new))   
    return answer
"""
# 정확도 10에서 시간초과가 발생, 스택으로 이용해야하는 이유이다. 근데 왜ㅠㅠ? 종료 조건을 확실히? 
# number를 list로 변경하면서 복잡도가 커짐
# del list[i] 연산자는 복잡도가 O(N)이다. pop(i)도 O(N)이다. 

# List 자료형은 삽입, 제거, 탐색, 포함 여부 확인 모두 O(n)에 해당하는 시간 복잡도를 가지고 있습니다.
# Set과 Dictionary는 삽입, 제거, 탐색, 포함여부확인 연산에 O(1)의 시간 복잡도를 가지고 있습니다.

# 탐색과 확인이 주로 필요한 연산이라면 Set이나 Dictionary를 사용하는 것이 좋고 
# 순서와 index에 따른 접근이 필요하다면 List 자료형을 사용하는 것이 좋을 것입니다. 

def solution(number, k):
    answer = ''
    i = 0
    number = list(map(int, number))
    
    n = len(number)
    while k > 0 and i+1 != len(number):
        if number[i] < number[i+1]:
            del number[i]
            k-=1
            if i != 0 :
                i -= 1
        else:
            i+=1
    if k > 0:
        answer = answer[:-k]
    answer = "".join(map(str,number))
    return answer
"""
def solution(number, k):
    i=0
    while i<len(number)-1 and k>0:
        if number[i]<number[i+1]:
            number = number[:i]+number[i+1:]
            if i!=0:
                i-=1
            k-=1
        else:
            i+=1
    if k>0:
        return number[:-k]
    return number
    
