# 알고리즘

- ### 문제 출처

  - 백준 https://www.acmicpc.net/
  - 프로그래머스 https://programmers.co.kr/
# 파이썬 문법

### 리스트 컴프리헨션 

: 리스트를 초기화하는 방법 중 하나이다. 리스트 컴프리헨션을 이용하면 대괄호([])안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있다. 

```python
Array = [i for i in range(20) if i % 2 == 1]
```

이러한 리스트 컴프리헨션은 코딩테스트에서 2차원 리스트를 초기화할 때 매우 효과적으로 사용될 수 있다. 


#### N * M 크기의 2차원 리스트 초기화

```python
N = 3
M = 4
array = [[0] * m for _ in range(n)]
```

### 튜플 자료형 

튜플 자료형은 그래프 알고리즘을 구현할 때 자주 사용된다. 예를 들어 다익스트라 최단 경로 알고리즘에서 우선순위 큐에 한 번 들어간 값을 변경되지 않는다. 그래서 그 우선 순위 큐에 들어가는 데이터를 튜플로 구성하여 소스 코드를 작성한다. **‘비용’과 ‘노드 번호’라는 서로 다른 성질의 데이터를 (비용, 노드 번호)의 형태로 함께 튜플로 묶어서 관리하는 것이 관례이다.**

### 집합 자료형

사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다는 특징이 있다. 특정 원소가 존재하는지를 검사하는 연산의 시간 복잡도는 사전 자료형과 마찬가지로 O(1)이다. **특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 매우 효과적이다.** 
집합 자료형의 연산 : 기본적인 집합 연산으로는 합집합, 교집합, 차집합이 있다.

```python
print(a | b) #합집합 print(a & b) #교집합 print(a - b) #차집합

a.add(4), a.remove(4) 함수 모두 시간 복잡도가 O(1)이다.
```

### 입력을 위한 전형적인 소스코드

```
N = int(input())
Data = list(map(int , input().split()))


n, m, k = map(int, input().split())

import sys
data = sys.stdin.readline().rstrip()
```

### 주요 라이브러리의 문법과 유의점

#### 내장함수

- result = sorted(list, key = lambda x : x[1], reverse = True)
  result.sort()

- itertools : 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다. 순열과 조합 라이브러리를 제공한다.

- Permutations, combinations, product

- headq : 힙 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.
  최소 힙으로 구성되어 있으므로 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차운 정렬이 완료된다. 최상단 원소는 항상 ‘가장 작은’ 원소이기 때문이다. **삽입을 할 때는 heapq.heappush(h,value), 원소를 꺼내고자 할 때는 heapq.heappop(h) 메소드를 이용한다.**  

- bisect : 이진 탐색 기능을 제공하는 라이브러리이다. 

- collections : 덱(deque), counter 등의 유용한 자료구조를 포함하고 있는 라이브러리이다. 
  Deque의 경우, 가장 앞쪽/뒤쪽에 있는 원소 제거/추가의 시간 복잡도는 O(1)이다. Deque에서는 리스트 자료형과 다르게, 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다. popleft(), pop(), appendleft(), append() 을 사용한다. 
  Counter는 등장 횟수를 세는 기능을 제공한다.

  ```python
  From collections import Counter
  counter= Counter([‘red’, ‘blue’, ’red’, ‘green’, ‘blue’, ‘blue’])
  print(counter[‘blue’]) # 3
  print(dict(counter)) # {‘red’ :2 , ‘blue’ : 3, ‘green’ : 1} 
  ```

- math : 필수적인 수학적 기능을 제공하는 라이브러리이다.

