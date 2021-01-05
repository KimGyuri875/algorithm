import heapq

def solution(scoville, K):
    answer = 0
    heap  = []
    for i in scoville:
        heapq.heappush(heap,i)        # heapq.heapify(scoville) 으로 간략하게 사용 가능.

    while len(heap):
        if heap[0] >=K:
            return answer

        sum =  heapq.heappop(heap)
        if heap != []:
            sum += heapq.heappop(heap) * 2
            heapq.heappush(heap,sum)
            answer += 1

    return -1
    
    '''
    heappop을 두번 연속으로 할 경우 오류가 발생하는 걸 간과해서는 안된다. 
    heappop을 한번한 뒤에 heap이 비어 있는지 확인을 해야 한다. 
    '''
