# 내가 생각한 방식 : slicing을 생각했지만 인덱스가 벗어나면 오류가 발생할거라고 생각함. 또 깊이 생각을 못함. prev을 통해 비교할 대상을 upgrade해야함을 놓침. 
# str()을 통해 count을 감싸주면서 꼼꼼한 풀이가 돋보인다. 
# com을 형성하는 방식을 눈여겨 보자.
# 꼼꼼한 풀이! input의 길이 1000으로 완전탐색을 구현해도 됨을 인지하자.
# 정답풀이
"""
2020 카카오공채에 출제되었던 문제이다. 먼저 문자열을 몇개 단위로 짜를지에 대해 cut을 이용하는 제일 바깥 for문을 1, len(s) // 2 + 1까지 반복했다. 
문자열을 꼭 2로 나누어 문자열 길이보다 더 넘어가는 비교는 할 필요 없도록 한다. 
그리고 tempStr에 cut만큼 짤라낸 문자열을 대입해 다음 문자열들과 cut 단위로 비교한다.
(s[i:i+cut]) 같으면 count를 +1 해주고, 
틀리면 count와 비교했던 tempStr을 result값에 넣어주면 된다. 
그리고 중요한 것이 마지막에 한번 더 result에 count + tempStr을 넣어줘야 
제일 마지막으로 비교했던 문자열이 들어갈 수 있다.
"""
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
        answer = min(answer, len(com))                          # 이방법 대신 그냥 len()을 list에 넣고 min() return하면 된다.  
      
    return answer         
        
