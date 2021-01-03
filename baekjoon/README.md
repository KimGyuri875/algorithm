# BOJ 백준 알고리즘

### DynamicProgramming(동적계획법) 

> ####  n에 대해 최초로 답을 구했을 때, 어딘가에 답을 적어둔다. 다시 만났을 때 그 답을 활용.

- 백준 2747 피보나치 수 https://www.acmicpc.net/problem/2747

  피보나치 수열을 재귀함수로 함수가 2개의 함수를 호출하면서 시간 복잡도가 O(2^n)이 된다. 같은 값을 반복해서 사용하니깐 동적 계획법을 사용한다. 


### Queue (큐)

> `list`: 무작위 접근에 최적화된 자료 구조이기 때문에 `pop(0)`, `insert(0,x)`의 복잡도는 O(N)이다. 
>
> `deque`: `popleft()`와 `appendleft(x)`메서드는 O(1)의 복잡도를 가진다. 하지만 i번째 데이터에 접근하는 복잡도는 O(N)이다. 
>
> `Queue`: `from queue import Queue`을 해줘야 한다.  `put(x)`, `get()` 데이터 추가/삭제는 O(1), 데이터 접근은 O(N)이다.  

- 백준 18258 큐 2 https://www.acmicpc.net/problem/18258

  list를 쓰니깐 시간초과 발생. -> deque 와, sys.stdin.readline() 을 사용한다. 
    
  
### Stack (스택)

> `list`  or `deque`
>
- 백준 10826 스택
