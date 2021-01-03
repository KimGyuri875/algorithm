import sys
from collections import deque

count = 0
N, M = map(int,sys.stdin.readline().split())

deq = deque()
for i in range(N):
    deq.append(i + 1)
a = map(int,sys.stdin.readline().split())

for i in a:
    j = 0
    while i != deq[j]:
        j += 1
    if len(deq) - j < j:
        j = len(deq) - j
    else:
        j = -j
    print(j)
    deq.rotate(j)
    count += abs(j)
    deq.popleft()

print(count)
     
















"""
a = list(map(int,sys.stdin.readline().split()))
q = [i for i range(1, N+1)]
for i in range(M):
    q_len = len(q)
    q_index = q.index(a[i])
    # head에 가까운지 tail에 가까운지 check
    if q_index < q_len - q_index:
        while True:
            if q[0] == s[i]:
                del q[0]
                break
            else:
                #head으로 이동
                q.append(q[0])
                del q[0]
                count += 1
    else:
        while True:
            if q[0] == s[i]:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                break

print(count)
"""