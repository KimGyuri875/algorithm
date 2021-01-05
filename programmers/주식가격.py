def solution(prices):
    answer = []
    
    # answer = [0] * len(prices) 으로 초기화하면 마지막 줄 생략가능하고 깔끔하다
    for i in range(len(prices)-1):
        count = 0
        for j in range (i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                answer.append(count)
                break;
            if j == len(prices)-1:
                answer.append(count)

    answer.append(0)
    return answer
    
    '''
    prices = deque(prices)
    c = prices.popleft()
    으로 deque를 이용할 수 있다. 
    '''
