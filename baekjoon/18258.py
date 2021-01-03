import sys
from collections import deque
N = int(sys.stdin.readline()) 
# sys.stdin.readline() 시간제한 있을 때 쓴다.
a = deque() 
while N > 0:
    task = sys.stdin.readline().split()
    if task[0]=="push":
        a.append(task[1])
    elif task[0]=='pop':
        if len(a)==0:
            print("-1") 
        else:
            print(a.popleft())
    elif task[0]=='size':
        print(len(a))
    elif task[0]=='empty':
        if len(a)==0:
            print("1") 
        else:
            print("0")
    elif task[0]=='front':
        if len(a)==0:
            print("-1") 
        else:
            print(a[0])
    elif task[0]=='back':
        if len(a)==0:
            print("-1") 
        else:
            print(a[-1])
    N-=1