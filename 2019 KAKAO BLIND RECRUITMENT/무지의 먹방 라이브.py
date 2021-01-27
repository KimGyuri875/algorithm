# 1. 내가 처음 풀이한거는 sort을 통해서 가장 작은 값을 빼주고 다시 sort하는 방식 => 효율성 X
# 2. 단순하게 while 문으로 -1을 직접 해주는 방식 => 정확성, 효율성 X
# 3. 우선순위 큐를 통해. 우선순위 큐는 일반적인 큐의 순서대로 원소를 제거하는 선입선출(FIFO) 방식이 아니라, 
# 순서에 상관없이 추가가 되어도 값을 뽑을 때는 가장 작은값(오름차순,우선순위)을 제거하는 특성을 지닌 자료 구조.
# 정답 풀이
from queue import PriorityQueue
def solution(food_times, k):
    answer = []
    key = 0

    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i+1))
        
    # 가장 작은 수가 맨 앞으로 간 결과를 확인 할 수 있다. 정렬은 아니다. 
    #print(q.queue)

    sum_value = 0
    previous = 0 
    length = len(food_times)
    
    # 미리 확인을 하는 방법으로, 만약 이 결과로 k의 범위를 넘어설 경우를 막는다.
    while sum_value + ((q.queue[0][0] - previous) * length) <= k:
        now = q.get()[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    answer = sorted(q.queue, key = lambda x : x[1])
    
    # 굉장히 인상깊은 방법으로, k의 범위를 넘어서지 않도록 sum_value를 설계했기 때문에 
    #나머지가 출력되는 % 연산자를 이용해서 다음으로 먹어야 할 음식을 출력할 수 있다. 
    return answer[(k - sum_value) % len(q.queue)][1]


# 2. --------------------------------------------------
def solution(food_times, k):
    answer = 0
    key = 0
    
    while k > 0:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            food_times[i] -= 1
            k -= 1
            if k == 0:
                key = i
                break
                
    print(food_times)
    i = key + 1
    while True:
        if i >= len(food_times):
            i = 0
        if i == key:
            if food_times[i] > 0:
                return i+1
            return -1
        if food_times[i] > 0:
            return i+1
