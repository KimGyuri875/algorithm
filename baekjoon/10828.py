import sys
from collections import deque
N = int(sys.stdin.readline()) 
# sys.stdin.readline() 시간제한 있을 때 쓴다.
stack = deque() 
while N > 0:
    task = sys.stdin.readline().split()
    if task[0]=="push":
        stack.appendleft(task[1])
    elif task[0]=='pop':
        if len(stack)==0:
            print("-1") 
        else:
            print(stack.popleft())
    elif task[0]=='size':
        print(len(stack))
    elif task[0]=='empty':
        if len(stack)==0:
            print("1") 
        else:
            print("0")
    elif task[0]=='top':
        if len(stack)==0:
            print("-1") 
        else:
            print(stack[0])
    N-=1