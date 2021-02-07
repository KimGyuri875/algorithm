# 내가 생각한 방식 : slicing을 생각했지만 인덱스가 벗어나면 오류가 발생할거라고 생각함. 또 깊이 생각을 못함. prev을 통해 비교할 대상을 upgrade해야함을 놓침. 
# str()을 통해 count을 감싸주면서 꼼꼼한 풀이가 돋보인다. 
# com을 형성하는 방식을 눈여겨 보자.
# 꼼꼼한 풀이! input의 길이 1000으로 완전탐색을 구현해도 됨을 인지하자.
# 정답풀이

def solution(s):
    answer = len(s)
    length = len(s)//2+1

    for step in range(1, length):
        com = ""
        count = 1
        prev = s[0:step]
        for j in range(step,len(s), step):
            if prev == s[j:j+step]:
                count+=1
            else :
                com+= str(count)+prev if count >=2 else prev
                count = 1
                prev = s[j:j + step] # 다시 상태 초기화
        # str()을 통해 count을 감싸주면서 꼼꼼한 풀이가 돋보인다. 
        # com을 형성하는 방식을 눈여겨 보자.
        com+= str(count)+prev if count >=2 else prev
        answer = min(answer, len(com))
            
    return answer         
        
