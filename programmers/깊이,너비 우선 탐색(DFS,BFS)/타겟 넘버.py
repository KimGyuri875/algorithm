def solution(numbers, target):
    answer = 0
    level = len(numbers)
    def dfs(depth, total):
        if depth == level:
            if total == target:
                nonlocal answer
                answer += 1
        else:
            dfs(depth+1, total + numbers[depth])
            dfs(depth+1, total - numbers[depth])
    dfs(0, 0)
    return answer


"""
# 가지치기가 한눈에 잘보이는 코드 

def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)
"""
'''
# 타겟 넘버
# n개의 음이 아닌 정수 + or - = target

import sys
from collections import deque

input = sys.stdin.readline

numbers = list(map(int , input().split()))
target = int(input())
deq = deque()
deq.append([numbers[0], 0,0,1]) # result, +개수,-개수, 연산횟수
deq.append([-1 * numbers[0], 0,0,1])
cnt = 0
while deq:
    p = deq.pop()
    if p[3] == len(numbers):
        if p[0] == target:
            print(p)
            cnt+=1
    else:
        deq.append([p[0]+numbers[p[3]], p[1]+1, p[2], p[3] + 1])
        deq.append([p[0]-numbers[p[3]], p[1], p[2]+1, p[3] + 1])


print(cnt)
'''
