from collections import deque
num = input()
stack0 = deque()
stack1 = deque()
for idx, num in enumerate(num):
    if num == '0':
        if stack0 and stack0[-1] == idx-1:
            stack0.pop()
        stack0.append(idx)
    else:
        if stack1 and stack1[-1] == idx-1:
            stack1.pop()
        stack1.append(idx)


if len(stack1) > len(stack0):
    print(len(stack0))
else:
    print(len(stack1))
    
"""
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))

"""
